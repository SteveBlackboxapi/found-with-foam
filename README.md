# Found with Foam — Volume One

A responsive web edition of the magazine for Sixteenth. Plain HTML, CSS and a small navigation script; no build step or third-party runtime requests.

## Preview

From this directory, run `python3 -m http.server 4173`, then open http://localhost:4173.

The issue works without JavaScript. JavaScript adds the active chapter indicator. Navigation stays visible on mobile, and reduced-motion preferences disable smooth scrolling.

## Checks

```sh
python3 tests/check_site.py
node --check script.js
git diff --check
```

These are static integrity checks, not a substitute for a visual browser review. Review the cover and all chapters at desktop, tablet and phone widths, test keyboard navigation and the PDF download, and check for horizontal overflow.

## Publishing

The existing GitHub Actions workflow publishes `main` to GitHub Pages. In repository Settings → Pages, the source must be **GitHub Actions**. The expected URL is https://steveblackboxapi.github.io/found-with-foam/.

That URL returned HTTP 404 during this repair. A successful deployment and a live URL check are still required before sharing it. HTML Preview is not the canonical host: it can handle scripts, styles and assets differently from normal hosting.

## Content and assets

- The source issue is available at `assets/documents/found-with-foam-volume-one.pdf`.
- The original cover, talent results, fitness image, skincare imagery and media-kit screenshot come from the supplied PDF.
- The overhead hero is an AI-generated photographic mockup made with the supplied cover and table references. The small print in that mockup is a generated reproduction; the original cover and downloadable PDF preserve the source artwork.
- See `docs/hero-art-direction.md` for the full generation prompt.
- DM Sans is self-hosted under its included SIL Open Font License.
- All product calls to action use the destinations embedded in the PDF: Talent Directory, Explore Content and Media Kits. Product access may require signing in to Foam.
- Search queries and timestamps are editorial examples. The highlighted skincare result links to its explanatory panel; actual content search and playback happen in Foam.
