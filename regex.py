import re
import sys
# with open("sample.txt","r") as file:
#     for line in file:
#         if re.search("SMS", line):
#             a = line.rstrip()
#             print(a)


with open("sample.txt","r") as file:
    for line in file:
        if re.search("SMS", line):
            a = line.rstrip()
            filename = open("out.txt","a")
            filename.write(a + "\n")
            filename.close


# file_path = 'out.txt'
# sys.stdout = open(file_path, "w")
# print("anto")
