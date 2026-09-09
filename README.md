# Woshico

A plain HTML, CSS, and JavaScript rebuild of the Woshico car-wash marketing site. It includes the responsive landing page, service pages and detail routes, about, projects, journal and article routes, pricing tabs, FAQ, contact form, shop/checkout paths, team, and utility pages with client-side navigation and a static-host fallback.

## Run locally

```bash
python3 -m http.server 4173
```

Then open `http://localhost:4173/`.

## Deploy

The site has no build step and is configured to deploy automatically to GitHub Pages from `main` via `.github/workflows/pages.yml`. The expected public URL is:

`https://abdulanasbuilds.github.io/Auto-detailing/`

Visual media is referenced from the original public Webflow CDN, so the repository stays lightweight and does not depend on local-only storage.
