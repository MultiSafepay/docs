import re
from pathlib import Path

PATH = ['{0}/content'.format(Path(__file__).parent.parent),'{0}/api'.format(Path(__file__).parent.parent)]

regex = "\[([^\[\]]*)\]\((https?:\/\/[\w\d./?=#&\+%-]+)\)"


def main():
    external_md = False
    for path in PATH:
      for file in walk(path):
          with open(file, 'r') as f:
              content = f.read()
              result = re.finditer(regex, content)
              if result is not None:
                  for res in result:
                      print('External link found {0} in file {1}'.format(
                          res.group(0), file))
                      external_md = True
    return external_md

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