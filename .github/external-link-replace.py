import re
from pathlib import Path
import os

PATH = str.split(os.environ.get("DOCS_PATHS"))

regex = re.compile(r'\[([^\[\]]*)\]\((https?:\/\/[\w\d./?=#&\+%-]+)\)')
replacement = r'<a href="\2" target="_blank">\1</a> <i className="fa fa-external-link" <i className="fa fa-external-link" style={{ fontSize:\'12px\', color:\'#8b929e\' }}></i>'


def main():
    print('List of files: {0}' .format(PATH))
    for file in PATH:
        print('Working on: {0}' .format(file))
        replace_urls(file)


ignore_files = []


def replace_urls(file_name):
    with open(file_name, 'r') as file:
        filedata = file.read()
        filedata = re.sub(regex, replacement, filedata)

        with open(file_name, 'w') as file:
            file.write(filedata)
            file.close()

if __name__ == "__main__":
    if main():
        raise ValueError
