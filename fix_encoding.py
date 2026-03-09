#!/usr/bin/env python3
import re

with open('chapters/examples/chapter03.tex', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all problematic Unicode characters
replacements = {
    '\u201c': '``',      # left double quote
    '\u201d': "''",      # right double quote  
    '\u2018': "'",       # left single quote
    '\u2019': "'",       # right single quote
    '\u2013': '--',      # en dash
    '\u2014': '---',     # em dash
    '\u2011': '-',       # non-breaking hyphen
    '\u2012': '-',       # figure dash
    '\u00ad': '',        # soft hyphen
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open('chapters/examples/chapter03.tex', 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed all problematic characters in chapter03.tex')
