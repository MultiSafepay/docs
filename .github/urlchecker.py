import re
from pathlib import Path

# This script checks links to markdown anchors in headers. If the link contains a / at the end, an error is raised.

PATH = ['{0}/content'.format(Path(__file__).parent.parent),'{0}/api'.format(Path(__file__).parent.parent)]

regex = '(\/[\w\-\.]+)+\/#[\w\-\.]+[\/]|#[\w\-\.]+[\/]'


def main():
    markdownlink = False
    for path in PATH:
      for file in walk(path):
          with open(file, 'r') as f:
              content = f.read()
              result = re.finditer(regex, content)
              if result is not None:
                  for res in result:
                      print('The following markdown URL: {0} in file {1} is incorrect. '
                            'A \'/\' at the end of the URL is not allowed.'.format(res.group(0), file))
                      markdownlink = True
    return markdownlink

ignore_files = []

def walk(start):
    paths = []
    for filename in Path(start).glob('**/*.md'):
        if any(path in str(filename) for path in ignore_files):
            continue
        paths.append(filename)
    return paths


if __name__ == "__main__":
    if main():
        raise ValueError
