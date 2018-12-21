# Kimberly Vo
# kv3nw

import re

nospace = re.compile(r'\S+')

quotation = re.compile(r'["]\S[A-z\s]+\S["]')

twonum = re.compile(r'(\-?[0-9]+([.]?[0-9]+)?)[,]?[ ]?(\-?[0-9]+([.]?[0-9]+)?)')
