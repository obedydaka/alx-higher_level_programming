#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit()

argumts = "{:d} argument"
argc = len(sys.argv) - 1
if argc == 0:
    argumts += 's.'
elif argc == 1:
    argumts += ':'
else:
    argumts += 's:'
print(argumts.format(argc))

i = 0
for argument in sys.argv:
    if i != 0:
        print("{:d}: {:s}".format(i, argument))
    i += 1
