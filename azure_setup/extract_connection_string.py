#! /usr/bin/python3.8

import re
import sys

stdin = sys.stdin.read()
line = list(el.strip() for el in stdin.split("\n"))[3]
connection_string = re.match(r'"connectionString": "(.*)",', line).group(1)
print(connection_string)
