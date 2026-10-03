"""
Extract XiaoHongShu (小红书) note content.
Detects note type (normal/image vs video) and extracts accordingly.
Usage: python xhs_scraper.py <url>
Output: JSON to stdout.
  - normal/image notes: title, author, text, images (url list)
  - video notes: title, author, text (description/captions), video_url, note_type='video'

Strategy: mobile site (m.xiaohongshu.com) first — its __INITIAL_STATE__ contains
normalNotePreloadData which reliably carries title/desc/images for share links.
Falls back to desktop noteDetailMap structure.
"""
import sys, json, re, urllib.request

MOBILE_UA = ('Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) '
             'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1')
DESKTOP_UA = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
              '(KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36')


def fetch(url, ua, timeout=25):
    headers = {
        'User-Agent': ua,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode('utf-8', errors='replace')


def extract_state(page):
    match = re.search(r'window\.__INITIAL_STATE__\s*=\s*({.*?})\s*</script>', page, re.DOTALL)
    if not match:
        match = re.search(r'window\.__INITIAL_STATE__\s*=\s*({.*?})\s*\n', page, re.DOTALL)
    if not match:
        return None
    raw_json = match.group(1)
    raw_json = re.sub(r':\s*undefined', ': null', raw_json)
    return raw_json


def find_json_value(raw, key):
    """Locate a top-level-ish JSON value by key in raw INITIAL_STATE text."""
    idx = raw.find('"' + key + '"' + ':')
    if idx < 0:
        return None
    dec = json.JSONDecoder()
    try:
        val, _ = dec.raw_decode(raw[idx + len('"' + key + '"' + ':'):])
        return val
    except Exception:
        return None


def parse_mobile(raw):
    """Parse mobile INITIAL_STATE: normalNotePreloadData + profile.userInfo.nickName."""
    preload = find_json_value(raw, 'normalNotePreloadData')
    if not preload or not preload.get('title'):
        return None
    title = preload.get('title', '')
    desc = preload.get('desc', '')
    images = []
    for i, img in enumerate(preload.get('imagesList', [])):
        # Prefer the large version
        img_url = img.get('urlSizeLarge') or img.get('url') or ''
        if img_url.startswith('http://'):
            img_url = img_url.replace('http://', 'https://', 1)
        images.append({'index': i, 'url': img_url})
    # Author nickname from profile.userInfo (or any nickName in page)
    author = ''
    profile = find_json_value(raw, 'profile')
    if profile and profile.get('userInfo', {}).get('nickName'):
        author = profile['userInfo']['nickName']
    if not author:
        m = re.search(r'"nickName":"([^"]*)"', raw)
        if m:
            author = m.group(1)
    # note id
    note_id = ''
    m = re.search(r'"noteId":"([^"]*)"', raw)
    if m:
        note_id = m.group(1)
    return {
        'title': title,
        'author': author,
        'text': desc,
        'images': images,
        'note_type': 'normal',
        'is_video': False,
        'note_id': note_id,
        'source': 'mobile',
    }


def parse_desktop(raw):
    """Parse desktop INITIAL_STATE: note.noteDetailMap (legacy fallback)."""
    data = json.loads(raw)
    note_detail_map = data.get('note', {}).get('noteDetailMap', {})
    if not note_detail_map:
        return None
    note_key = list(note_detail_map.keys())[0]
    note = note_detail_map[note_key].get('note', {})

    note_type = note.get('type', 'normal')
    is_video = (note_type == 'video')

    title = note.get('title', note.get('displayTitle', ''))
    desc = note.get('desc', '')
    author_info = note.get('user', {})
    author = author_info.get('nickname', '') or author_info.get('nickName', '')

    images = []
    image_list = note.get('imageList', [])
    for i, img in enumerate(image_list):
        img_url = img.get('urlDefault', img.get('url', '')) or img.get('infoList', [{}])[-1].get('url', '')
        if img_url:
            if img_url.startswith('http://'):
                img_url = img_url.replace('http://', 'https://', 1)
            images.append({'index': i, 'url': img_url})

    result = {
        'title': title,
        'author': author,
        'text': desc,
        'images': images,
        'note_type': note_type,
        'is_video': is_video,
        'source': 'desktop',
    }

    if is_video:
        video_info = note.get('video', {})
        media = video_info.get('media', {})
        stream = media.get('stream', {})
        video_url = ''
        for quality in ['h264', 'h265']:
            for level in ['1080p', '720p', '480p']:
                for s in stream.get(quality, []):
                    if s.get('width') and level in str(s.get('width')):
                        video_url = s.get('masterUrl', '')
                        if video_url:
                            break
                if video_url:
                    break
            if video_url:
                break
        if not video_url:
            for hw in ['h264', 'h265']:
                for s in stream.get(hw, []):
                    video_url = s.get('masterUrl', '')
                    if video_url:
                        break
                if video_url:
                    break
        result['video_url'] = video_url
        duration = media.get('video', {}).get('duration', 0) or video_info.get('duration', 0)
        result['duration'] = duration

    return result


def scrape(url):
    # Rewrite www → m for the mobile attempt
    mobile_url = url.replace('www.xiaohongshu.com', 'm.xiaohongshu.com')
    # Mobile attempt
    try:
        page = fetch(mobile_url, MOBILE_UA)
        raw = extract_state(page)
        if raw:
            result = parse_mobile(raw)
            if result:
                return result
    except Exception:
        pass

    # Desktop fallback
    try:
        page = fetch(url, DESKTOP_UA)
        raw = extract_state(page)
        if raw:
            result = parse_desktop(raw)
            if result:
                return result
    except Exception:
        pass

    return {'error': 'note data not found — xsec_token may be missing or expired'}


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
