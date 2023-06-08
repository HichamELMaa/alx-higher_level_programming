#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = sys.argv[1:]
    index = 1

    if len(arguments) == 0:
        print('No arguments.')
    else:
        print('{} arguments:'.format(len(arguments)))

    for argument in arguments:
        print('{}: {}'.format(index, argument))
        index += 1
