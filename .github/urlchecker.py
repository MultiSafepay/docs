import re
from pathlib import Path
from operator import itemgetter
import requests

IGNORE_CODE = [200, 301, 302, 999]

LINK_TEMP = 'HTTP Status: {0}, \t url:{1}, \t Document: {2}'
PATH = '{0}/content'.format(Path(__file__).parent.parent)
ROOT_URL = 'http://docs.multisafepay.com'


def main():
    status = False
    path = PATH
    root_url = ROOT_URL

    ## find links in markdown files
    links = []
    for path in walk(path):
        for link in find_links(path):
            if link[1].startswith('/'):
                l = root_url + link[1]
            elif link[1].startswith('#'):
                continue
            elif link[1].find('png') >= 0 or link[1].find('mailto') >= 0:
                continue
            else:
                l = link[1]

            try:
                r = requests.get(l, allow_redirects=True, timeout=10)
                if r.status_code not in IGNORE_CODE:
                    if r.status_code != 404 and not 'multisafepay.com' in l:
                        continue
                    links.append([str(r.status_code), str(l), str(path)])
                else:
                    continue
            except:
                if 'https://www.shopify.com/login?redirect' in l: # If it happens with more links, add function to check
                    print('{0} has hit the rate limit for request.'.format(l))
                else:
                    links.append(['error', str(l), str(path)])

    links = sorted(links, key=itemgetter(1))

    if len(links) > 0:
        status = True
        for link in links:
            print(link)
    return status


def walk(start):
    paths = []
    for filename in Path(start).glob('**/*.md'):
        paths.append(filename)
    return paths


def get_content(path):
    with open(path, 'r') as content_file:
        return content_file.read()


def find_links(path):
    content = get_content(path)
    name_regex = "[^]]+"
    url_regex = "[^)]+"
    markup_regex = '\[({0})]\(\s*({1})\s*\)'.format(name_regex, url_regex)

    matches = []
    for match in re.findall(markup_regex, content):
        if match[1].startswith('<mailto:'):
            continue
        matches.append(match)

    return matches


if __name__ == "__main__":
    status = main()
    if status:
        raise ValueError
