# encoding: utf8

import os
import re

file_pattern = re.compile(r'\d{8}.+\.md')

source_files = []

for root, dirs, files in os.walk('.', topdown=False):
    for f in files:
        if file_pattern.match(f):
            source_files.append(f)


for f in source_files:
    _dir = os.path.join('docs/', f[:4])

    if not os.path.exists(_dir):
        os.makedirs(_dir)

    cmd = ' '.join(['mv', f, os.path.join(_dir, f)])
    print(cmd)
    os.system(cmd)
