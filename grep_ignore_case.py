import re
import sys

with open("sample.txt","r") as file:
    for line in file:
        regex_name = re.compile(r'tsel', re.IGNORECASE)
        if regex_name.search(line):
            a = line.rstrip()
            filename = open("out.txt","a")
            filename.write(a + "\n")
            filename.close
