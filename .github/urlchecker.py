import glob
import os
import re

# This script checks links to markdown anchors in headers. If the link contains a / at the end, an error is raised.

regex = '(\/[\w\-\.]+)+\/#[\w\-\.]+[\/]|\/#[\w\-\.]+[\/]'


def searcher():
    markdownlink = False

    for file in glob.glob(os.path.join('**/*.md'),recursive=True):
        with open(file, 'r') as f:
            content = f.read()
            result = re.finditer(regex, content)
            if result is not None:
                for res in result:
                    print('The following markdown URL: {0} in file {1} is incorrect. '
                          'A \'/\' at the end of the URL is not allowed.'.format(res.group(0), file))
                    markdownlink = True
    return markdownlink

if searcher():
    raise ValueError
