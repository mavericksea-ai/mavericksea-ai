"""Refresh public external PRs only. Run with --fixture for the saved preview data."""
import argparse
import datetime as dt
import html
import json
from pathlib import Path
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
START, END = '<!-- activity:start -->', '<!-- activity:end -->'

def fetch(state, limit):
    query = f'author:mavericksea-ai is:pr is:{state} is:public -org:driftproofhq -user:mavericksea-ai'
    url = 'https://api.github.com/search/issues?' + urllib.parse.urlencode({'q': query, 'sort': 'updated', 'per_page': limit})
    request = urllib.request.Request(url, headers={'Accept': 'application/vnd.github+json', 'User-Agent': 'mavericksea-ai-profile'})
    with urllib.request.urlopen(request, timeout=30) as response:
        data = json.load(response)
    if data.get('incomplete_results') or 'items' not in data:
        raise RuntimeError('Incomplete public search; preserving previous profile.')
    return data

def cell(items):
    rows = []
    for item in items[:3]:
        url = item['html_url']
        if not url.startswith('https://github.com/'):
            raise ValueError('Unexpected link')
        repo = '/'.join(url.split('/')[3:5])
        rows.append(f'<p><a href="{html.escape(url, quote=True)}"><b>{html.escape(repo)} #{item["number"]}</b></a><br/><sub>{html.escape(item["title"])}</sub></p>')
    return '\n'.join(rows) or '<p>No matching public PRs.</p>'

def build(merged, opened, day):
    return f'''{START}
<table>
<tr><td width="50%" valign="top"><h3>↗ Recently active · merged</h3>
{cell(merged['items'])}
</td><td width="50%" valign="top"><h3>◌ Under review</h3>
{cell(opened['items'])}
</td></tr>
</table>
<sub>Public external PRs · ordered by latest activity · refreshed {day} UTC.</sub>
{END}'''

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--fixture', action='store_true')
    args = parser.parse_args()
    if args.fixture:
        merged = json.loads((ROOT / 'merged-public.json').read_text())
        opened = json.loads((ROOT / 'open-public.json').read_text())
    else:
        merged, opened = fetch('merged', 3), fetch('open', 3)
    path = ROOT / 'README.md'
    before = path.read_text()
    if before.count(START) != 1 or before.count(END) != 1:
        raise ValueError('Expected exactly one activity block')
    day = dt.datetime.now(dt.timezone.utc).date().isoformat()
    after = before[:before.index(START)] + build(merged, opened, day) + before[before.index(END)+len(END):]
    path.write_text(after)
    print('Updated public activity block.')
