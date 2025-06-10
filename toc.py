# encoding: utf8

"""
生成目录
"""

import os

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
DOC_DIR = os.path.join(CUR_DIR, 'docs')
README = """
# 华为公司文件 

![自古英雄多磨难](自古英雄多磨难.jpg)
"""


def generate_toc():
    filepaths = []
    for root, dirs, files in os.walk(DOC_DIR):
        for name in files:
            filepaths.append(os.path.join(root, name))

    filepaths = [path.split('huawei/docs/')[1] for path in filepaths]
    filepaths = filter(lambda x: x.endswith('md'), filepaths)
    toc = {}

    for path in filepaths:
        year, filename = path.split('/')
        toc.setdefault(year, [])
        toc[year].append(filename)

    global README
    print(README)
    for year in sorted(toc.keys(), reverse=True):
        docs = sorted(toc[year], reverse=True)
        print('\n### %s' % year)
        for doc in docs:
            print('* [%s]' % doc.split('.')[0] + '(' + os.path.join('docs', year, doc) + ')')


if __name__ == '__main__':
    generate_toc()
