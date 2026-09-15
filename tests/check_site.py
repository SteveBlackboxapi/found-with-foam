"""Check deployable files, navigation and accessible image metadata without dependencies."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re

ROOT = Path(__file__).resolve().parents[1]
errors = []


class SiteParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.links = []
        self.assets = []
        self.image_count = 0
        self.h1_count = 0

    def handle_starttag(self, tag, attributes):
        attr = dict(attributes)
        if 'id' in attr:
            if attr['id'] in self.ids:
                errors.append(f"Duplicate id: {attr['id']}")
            self.ids.add(attr['id'])
        if tag == 'h1':
            self.h1_count += 1
        if tag == 'a':
            self.links.append(attr.get('href', ''))
            if attr.get('target') == '_blank' and 'noopener' not in attr.get('rel', '').split():
                errors.append(f"Missing noopener: {attr.get('href')}")
        if 'src' in attr:
            self.assets.append(attr['src'])
        if 'srcset' in attr:
            self.assets.extend(candidate.strip().split()[0] for candidate in attr['srcset'].split(','))
        if tag == 'link' and attr.get('rel') in ('stylesheet', 'icon', 'preload'):
            self.assets.append(attr['href'])
        if tag == 'img':
            self.image_count += 1
            if 'alt' not in attr:
                errors.append(f"Missing image description: {attr.get('src')}")
            if not all(attr.get(key, '').isdigit() for key in ('width', 'height')):
                errors.append(f"Missing reserved image dimensions: {attr.get('src')}")


site = SiteParser()
site.feed((ROOT / 'index.html').read_text())
for href in site.links:
    parsed = urlsplit(href)
    if not href:
        errors.append('Empty link')
    elif href.startswith('#'):
        if unquote(href[1:]) not in site.ids:
            errors.append(f'Missing anchor target: {href}')
    elif not parsed.scheme:
        site.assets.append(parsed.path)

css = (ROOT / 'styles.css').read_text()
site.assets.extend(re.findall(r"url\(['\"]?([^)'\"]+)", css))
for asset in set(site.assets):
    if urlsplit(asset).scheme:
        errors.append(f'Unexpected externally hosted asset: {asset}')
    elif not (ROOT / unquote(asset)).is_file():
        errors.append(f'Missing local asset: {asset}')

if site.h1_count != 1:
    errors.append(f'Expected one document title, found {site.h1_count}')
if not (ROOT / 'assets/documents/found-with-foam-volume-one.pdf').read_bytes().startswith(b'%PDF-'):
    errors.append('Invalid PDF download')
if 'prefers-reduced-motion' not in css:
    errors.append('Missing reduced-motion support')

if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(site.links)} links, {len(site.ids)} anchors, {site.image_count} images and {len(set(site.assets))} local assets.')
