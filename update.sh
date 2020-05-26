#!/bin/sh

python move.py && python toc.py > README.md && git add . && git commit -m 'update' && git push origin master
