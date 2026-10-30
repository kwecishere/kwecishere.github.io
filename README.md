# Chucky Assets – SEO site

Static site for https://kwecishere.github.io that links every Chucky Assets pack to its itch.io store page.

- Edit `_build/catalog.json` (packs) and `_build/build.py` (collections, copy), then run `python3 _build/build.py`.
- Output: `index.html`, collection pages, `packs/<slug>/`, `sitemap.xml`, `robots.txt`, `404.html`.
- GitHub Pages: Settings → Pages → Deploy from a branch → `main` / `(root)`.
