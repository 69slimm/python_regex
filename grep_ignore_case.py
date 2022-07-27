import re
import sys

# This script to get a line sentence that has 'tsel' word that perform case-insensitive matching. 
# So the line has words like 'Tsel' or 'tseL' ord 'tSel' etc, it will print the line. 
# It has same function like bash command "grep -i" in linux

with open("sample.txt","r") as file:
    for line in file:
        regex_name = re.compile(r'tsel', re.IGNORECASE)
        if regex_name.search(line):
            a = line.rstrip()
            filename = open("out.txt","a")
            filename.write(a + "\n")
            filename.close
