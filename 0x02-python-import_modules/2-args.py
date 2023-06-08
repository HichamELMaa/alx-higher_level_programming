#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = sys.argv[1:]
    index = 0
    if len(arguments) == 0:
        print('{} arguments.'.format(len(arguments)))
    else:
        print('{} arguments:'.format(len(arguments)))
    for argument in arguments:
        print('{}: {}'.format(index+1, argument))
