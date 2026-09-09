# Woshico

A static, reference-faithful clone of the published Woshico Webflow site. The repository contains the complete page templates for the homepage, secondary pages, blog posts, pricing, FAQ, shop, checkout, utility pages, and hidden service-detail routes.

## Run locally

```bash
python3 -m http.server 4174
```

Open `http://localhost:4174/`.

## Deployment

There is no build step. Deploy the repository root to Cloudflare Pages/Workers static hosting, GitHub Pages, or any static host. The original public Webflow CDN is used for the source site’s images, video, fonts, icons, and interaction scripts; no Manus-local storage paths are used.
