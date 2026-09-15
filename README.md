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

The GitHub Actions workflow publishes `main` to GitHub Pages at https://steveblackboxapi.github.io/found-with-foam/. Pages is enabled with **GitHub Actions** as its source. The initial rebuild deployed successfully after pull request #1 was merged.

Changes on review branches are available in the local preview and deploy after merging to `main`.

## Product styling

The site shell uses Foam's supplied F icon, a cool grey surround, navy branding, rounded surfaces and blue navigation controls. The magazine retains its editorial typography and lime, black and sage chapter colors.

## Content and assets

- The source issue is available at `assets/documents/found-with-foam-volume-one.pdf`.
- The original cover, talent results, fitness image, skincare imagery and media-kit screenshot come from the supplied PDF.
- The overhead hero is an AI-generated photographic mockup made with the supplied cover and table references. The small print in that mockup is a generated reproduction; the original cover and downloadable PDF preserve the source artwork.
- See `docs/hero-art-direction.md` for the full generation prompt.
- DM Sans is self-hosted under its included SIL Open Font License.
- `assets/images/foam-app-icon.png` is the user-supplied product logo, preserved unchanged and used in the header, footer, favicon and home-screen icon.
- All product calls to action use the destinations embedded in the PDF: Talent Directory, Explore Content and Media Kits. Product access may require signing in to Foam.
- Search queries and timestamps are editorial examples. The highlighted skincare result links to its explanatory panel; actual content search and playback happen in Foam.
