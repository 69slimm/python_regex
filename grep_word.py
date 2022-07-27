import re
import sys

# sample.txt is the file that we read
# 'SMS' word is word that we looking for. So the looping will find every line in file that has SMS word
# using rstrip() built-in function to remove extra enter in every line that it printed

with open("sample.txt","r") as file:
    for line in file:
        if re.search("SMS", line):
            a = line.rstrip()
            filename = open("out.txt","a")
            filename.write(a + "\n")
            filename.close

