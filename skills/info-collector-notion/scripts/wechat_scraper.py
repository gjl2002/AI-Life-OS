"""
Extract WeChat (公众号) article content and images.
Usage: python wechat_scraper.py <url>
Output: JSON to stdout with title, author, text, and base64 images.
"""
import sys, json, re, urllib.request, base64
from html import unescape


def download_as_base64(img_url):
    """Download image and return base64 data URI."""
    try:
        req = urllib.request.Request(img_url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
        ext = 'png' if 'png' in img_url.lower() else 'jpeg'
        b64 = base64.b64encode(data).decode()
        return f"data:image/{ext};base64,{b64}"
    except Exception as e:
        return None


def scrape(url):
    # Fetch page
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode('utf-8')

    # Extract title
    title_m = re.search(r'<meta\s+property="og:title"\s+content="([^"]*)"', html)
    title = unescape(title_m.group(1)) if title_m else 'untitled'

    # Extract author
    author_m = re.search(r'<meta\s+property="og:article:author"\s+content="([^"]*)"', html)
    author = unescape(author_m.group(1)) if author_m else ''

    # Extract image URLs from data-src
    img_urls = re.findall(r'data-src="(https?://[^"]+)"', html)
    # Also try src
    if not img_urls:
        img_urls = re.findall(r'<img[^>]+src="(https?://[^"]+)"', html)

    # Download images as base64
    images = []
    for i, img_url in enumerate(img_urls):
        b64 = download_as_base64(img_url)
        if b64:
            images.append({'index': i, 'url': img_url, 'base64': b64})

    # Extract text content from HTML
    # Try to get content from js_content div
    body_m = re.search(r'id="js_content"[^>]*>(.*?)</div>\s*<script', html, re.DOTALL)
    if body_m:
        body = body_m.group(1)
    else:
        body_m = re.search(r'<div[^>]*class="rich_media_content[^"]*"[^>]*>(.*?)</div>\s*<script', html, re.DOTALL)
        body = body_m.group(1) if body_m else ''

    # Strip HTML tags for plain text
    text = re.sub(r'<[^>]+>', '', body)
    text = unescape(text)
    text = re.sub(r'\n{3,}', '\n\n', text).strip()

    result = {
        'title': title,
        'author': author,
        'text': text,
        'images': images,
    }
    return result


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(json.dumps({'error': 'URL required'}, ensure_ascii=False))
        sys.exit(1)
    try:
        result = scrape(sys.argv[1])
        print(json.dumps(result, ensure_ascii=False))
    except Exception as e:
        print(json.dumps({'error': str(e)}, ensure_ascii=False))
        sys.exit(1)
