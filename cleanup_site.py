from pathlib import Path
import re

RETIRED = (
    "/shop",
    "/pricing-plan",
    "/checkout",
    "/utility-pages/style-guide",
    "/utility-pages/licenses",
    "/utility-pages/changelog",
)

CLEANUP_JS = r'''<script>
(function () {
  var retired = ['/shop','/pricing-plan','/checkout','/utility-pages/style-guide','/utility-pages/licenses','/utility-pages/changelog'];
  retired.forEach(function (href) {
    document.querySelectorAll('a[href="' + href + '"]').forEach(function (a) {
      (a.closest('li') || a).remove();
    });
  });
  document.querySelectorAll('.w-webflow-badge,.w-commerce-commercecartwrapper,.w-commerce-commercecartopenlink,.w-commerce-commercecartcontainer-wrapper').forEach(function (el) { el.remove(); });
  document.querySelectorAll('body *').forEach(function (el) {
    var text = (el.textContent || '').trim();
    if (/^\$\s*[0-9][0-9,]*(?:\.[0-9]{1,2})?(?:\s*(?:USD|GHS))?$/i.test(text)) el.remove();
  });
  document.querySelectorAll('body *').forEach(function (el) {
    if (el.children.length === 0 && /subscribe\s+to(?:\s+our)?\s+newsletter/i.test((el.textContent || '').trim())) {
      var form = el.closest('form');
      if (form) form.remove();
      el.remove();
    }
  });
  document.querySelectorAll('body *').forEach(function (el) {
    if (el.children.length === 0 && /^utility\s+pages$/i.test((el.textContent || '').trim())) el.remove();
  });
})();
</script>'''


def clean_html(text: str) -> str:
    text = text.replace('<!-- This site was created in Webflow. https://webflow.com -->', '')
    text = re.sub(r'<meta\s+content=["\']Webflow["\']\s+name=["\']generator["\']\s*/?>', '', text, flags=re.I)
    text = text.replace(' - Webflow Ecommerce website template', '')
    text = text.replace('Webflow Ecommerce website template', '')
    text = text.replace('premium Webflow theme', 'premium theme')
    text = text.replace('Premium Webflow theme', 'Premium theme')
    text = re.sub(r'\s*"priceRange"\s*:\s*"[^"]*",?', '', text, flags=re.I)
    text = re.sub(r'\s*"priceCurrency"\s*:\s*"[^"]*",?', '', text, flags=re.I)
    text = re.sub(r'\s*"price"\s*:\s*"[^"]*",?', '', text, flags=re.I)

    for href in sorted(RETired := RETIRED, key=len, reverse=True):
        text = re.sub(
            r'<li\b[^>]*>\s*<a\b(?=[^>]*\bhref=["\']' + re.escape(href) + r'["\'])[^>]*>.*?</a>\s*</li>',
            '', text, flags=re.I | re.S
        )
        text = re.sub(
            r'<a\b(?=[^>]*\bhref=["\']' + re.escape(href) + r'["\'])[^>]*>.*?</a>',
            '', text, flags=re.I | re.S
        )

    if 'data-site-cleanup="1"' not in text:
        marker = CLEANUP_JS.replace('<script>', '<script data-site-cleanup="1">', 1)
        if re.search(r'</body>', text, re.I):
            text = re.sub(r'</body>', marker + '</body>', text, count=1, flags=re.I)
        else:
            text += marker
    return text

for path in Path('.').rglob('*.html'):
    path.write_text(clean_html(path.read_text(encoding='utf-8')), encoding='utf-8')

for folder in ('shop', 'pricing-plan', 'checkout', 'utility-pages'):
    root = Path(folder)
    if root.exists():
        for child in sorted(root.rglob('*'), key=lambda p: len(p.parts), reverse=True):
            if child.is_file() or child.is_symlink():
                child.unlink()
            elif child.is_dir():
                child.rmdir()
        root.rmdir()

Path('cleanup_site.py').unlink()
Path('.github/workflows/one-time-site-cleanup.yml').unlink()
