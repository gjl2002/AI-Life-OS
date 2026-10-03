"""
Extract JiKe (即刻) post content.
Usage: python jike_scraper.py <url>
  URL format: https://web.okjike.com/u/<user_id>/post/<post_id>
  or: https://m.okjike.com/originalPosts/<post_id>
Output: JSON to stdout with title, author, text, images (base64).
"""
import sys, json, re, urllib.request, base64, html as html_mod


def download_as_base64(img_url):
    """Download image and return base64 data URI."""
    try:
        req = urllib.request.Request(img_url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
        ext = 'jpeg'
        if 'png' in img_url.lower():
            ext = 'png'
        elif 'gif' in img_url.lower():
            ext = 'gif'
        elif 'webp' in img_url.lower():
            ext = 'webp'
        b64 = base64.b64encode(data).decode()
        return f"data:image/{ext};base64,{b64}"
    except Exception:
        return None


def scrape(url):
    # Convert web.okjike.com to m.okjike.com for mobile page
    mobile_url = url.replace('web.okjike.com', 'm.okjike.com')
    # Extract post_id from URL
    post_match = re.search(r'/post/([a-zA-Z0-9]+)', url)
    if not post_match:
        post_match = re.search(r'/originalPosts/([a-zA-Z0-9]+)', url)
    post_id = post_match.group(1) if post_match else ''
    if not mobile_url.startswith('https://m.okjike.com'):
        mobile_url = f'https://m.okjike.com/originalPosts/{post_id}'

    # Fetch mobile page
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    }
    req = urllib.request.Request(mobile_url, headers=headers)
    with urllib.request.urlopen(req, timeout=15) as resp:
        page = resp.read().decode('utf-8')

    # Extract __NEXT_DATA__
    match = re.search(
        r'<script id="__NEXT_DATA__"[^>]*type="application/json"[^>]*>(.*?)</script>',
        page, re.DOTALL
    )
    if not match:
        return {'error': 'Could not find __NEXT_DATA__ in page'}

    data = json.loads(match.group(1))

    # Navigate to post data
    props = data.get('props', {}).get('pageProps', {})
    post = props.get('post', props.get('data', {}))

    if not post:
        return {'error': 'Could not extract post data from __NEXT_DATA__'}

    # Extract author
    user = post.get('user', {})
    author = user.get('screenName', user.get('name', ''))

    # Extract text content
    text = ''
    content = post.get('content', '')
    if isinstance(content, str):
        text = content

    # Handle markdown-style content
    text = html_mod.unescape(text)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\n{3,}', '\n\n', text).strip()

    # Extract pictures
    images = []
    pics = post.get('pictures', [])
    for i, pic in enumerate(pics):
        # Try different URL fields
        img_url = pic.get('picUrl', pic.get('pic_url', pic.get('url', '')))
        if not img_url:
            # Check thumbnail
            img_url = pic.get('thumbnailUrl', pic.get('thumbnail_url', ''))
        if img_url:
            # Ensure https
            if img_url.startswith('//'):
                img_url = 'https:' + img_url
            elif img_url.startswith('http://'):
                img_url = img_url.replace('http://', 'https://', 1)
            b64 = download_as_base64(img_url)
            if b64:
                images.append({'index': i, 'url': img_url, 'base64': b64})

    # Generate title from first line or author
    title = text.split('\n')[0][:50] if text else ''
    if title:
        title = re.sub(r'[\\/:*?"<>|]', '', title)

    # Extract tags from topic
    topic = post.get('topic', {})
    tags = [topic.get('content', '')] if topic.get('content') else []

    result = {
        'title': f'{author}：{title}' if author else title,
        'author': author,
        'text': text,
        'images': images,
        'tags': tags,
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
