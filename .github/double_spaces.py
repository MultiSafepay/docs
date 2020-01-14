import re
from pathlib import Path

PATH = '{0}/content'.format(Path(__file__).parent.parent)


def main():
    status = False
    path = PATH
    for filename in walk(path):
        words_list = open_file(filename)
        for word in words_list:

            if not word:
                continue
            if '|' in word or '*' in word:
                continue
            match = re.search("([a-zA-Z] \s+[a-zA-Z])", word)
            if match is not None:
                status = True
                print('File {0} contains possible whitespaces in following sentence: {1}'.format(filename, word))
    return status


def walk(start):
    paths = []
    for filename in Path(start).glob('**/*.md'):
        if any(['_index.md' in str(filename), 'changelog.md' in str(filename)]):
            continue
        paths.append(filename)
    return paths


def open_file(file):
    with open(file, 'r') as file_content:
        return list(filter(None, file_content.read().splitlines()))


if __name__ == "__main__":
    current_status = main()
    if current_status:
        raise ValueError
