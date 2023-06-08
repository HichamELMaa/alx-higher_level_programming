import sys

def add_arguments(args):
    result = 0
    for arg in args:
        result += int(arg)
    return result

if __name__ == "__main__":
    result = add_arguments(sys.argv[1:])
    print(result)
