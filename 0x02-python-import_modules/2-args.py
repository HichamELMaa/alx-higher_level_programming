#!/usr/bin/python3
import sys
arguments = sys.argv[1:]
index = 1
if len(arguments) == 0:
    print(len(arguments), 'arguments.')
else:
    print(len(arguments), 'arguments:')
    for argument in arguments:
        print(index, ':', argument)
        index += 1
