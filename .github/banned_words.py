import re
from pathlib import Path

PATH = '{0}/content'.format(Path(__file__).parent.parent)


ignore_characters = ['http',
                'zoomable',
                '.multisafepay',
                'multisafepay.',
                '##',
                '-',
                '"',
                '**']

with open('.github/banned_words.txt', 'r') as f:
    banned_words = f.read().split('\n')


def main():
    status = False
    path = PATH
    for filename in walk(path):
        words_list = open_file(filename)
        for word in words_list:
            if not word:
                continue
            if any(char in word for char in ignore_characters):
                continue
            word = re.sub('[^a-zA-Z0-9 \n\.]', '', word)
            for banned_word in banned_words:
                match = re.search(r'\b{0}\b'.format(str(banned_word)), word)
                if match is not None:
                    status = True
                    print('In file {0} the following banned word is used : {1}'.format(filename, match.group()))
    return status


ignore_files = ['_index.md',
                'changelog.md',
                'api/']


def walk(start):
    paths = []
    for filename in Path(start).glob('**/*.md'):
        if any(path in str(filename) for path in ignore_files):
            continue
        paths.append(filename)
    return paths


def open_file(file):
    with open(file, 'r') as file_content:
        return list(filter(None, file_content.read().splitlines()))


if __name__ == "__main__":
    if main():
        raise ValueError
