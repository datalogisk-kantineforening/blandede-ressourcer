#!/usr/bin/env python3

with open('skabelon.svg') as f:
    skabelon = f.read().strip()

with open('menu.txt') as f:
    texts = f.read().strip().split('\n\n')

for text in texts:
    title = text.replace(' ', '_').split('\n')[0]
    foname = 'output/' + title + '.svg'
    with open(foname, 'w') as f:
        f.write(skabelon.replace('TEXT', text))
