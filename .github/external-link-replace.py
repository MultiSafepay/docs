import re
from pathlib import Path
import os

PATH = os.environ.get("PATHS")

regex = re.compile(r'\[([^\[\]]*)\]\((https?:\/\/[\w\d./?=#&\+%-]+)\)')
replacement = r'<a href="\2" target="_blank">\1</a> <i class="fa fa-external-link" style="font-size:12px;color:#8b929e"></i>'


def main():
    for path in PATH:
        for file in walk(path):
            print(file)
            replace_urls(file)


ignore_files = []


def replace_urls(file_name):
    with open(file_name, 'r') as file:
        filedata = file.read()
        filedata = re.sub(regex, replacement, filedata)

        with open(file_name, 'w') as file:
            file.write(filedata)
            file.close()


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
