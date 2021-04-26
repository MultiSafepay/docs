import glob
import os
import re

regex = '[\w\-\.]+@([\w-]+\.+[\w-]{2,4}\. *\n)|<[\w\-\.]+@([\w-]+\.+[\w-]{2,4}\.)> *\n' \
        '|<[\w\-\.]+@([\w-]+\.+[\w-]{2,4})>\. *\n'


def searcher():
    email = False

    for file in glob.glob(os.path.join('**/*.md'),recursive=True):
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

if searcher():
    raise ValueError
