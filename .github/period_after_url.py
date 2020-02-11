import glob
import os
import re

def searcher():
    periodafterurl = False

    for file in glob.glob(os.path.join('**/*.md'),recursive=True):
        with open(file, 'r') as f:
            content = f.read()
            result = re.finditer('(\/*\)).$', content)
            if result is not None:
                for res in result:
                    print('A period at the end of a URL is not allowed: {1}'.format(
                        res.group(0), file))
                    periodafterurl = True
    return periodafterurl


status = searcher()

if status is True:
    raise ValueError
