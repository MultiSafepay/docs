import re
from pathlib import Path

PATH = ['{0}/content'.format(Path(__file__).parent.parent),'{0}/api'.format(Path(__file__).parent.parent)]

regex = "[\w\-\.]+@[\w\-\.]+\.$|[\w\-\.]+@[\w\-\.]+\.\\\\|<[\w\-\.]+@[\w\-\.]+\.>$|<[\w\-\.]+@[\w\-\.]+>\.$|<[\w\-\.]+@[\w\-\.]+\.>\.$|>[\w\-\.]+@([\w\-\.]+){2,4}\.<"


def main():
    email = False
    for path in PATH:
      for file in walk(path):
          with open(file, 'r') as f:
              content = f.read()
              result = re.finditer(regex, content)
              if result is not None:
                  for res in result:
                      print('The following e-mail address {0} in file {1} is incorrect. '
                            'A dot at the end of the e-mail address is not allowed.'.format(
                          res.group(0), file))
                      email = True
    return email

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