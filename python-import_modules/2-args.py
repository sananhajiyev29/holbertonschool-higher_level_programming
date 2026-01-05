#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arg_count = len(argv) - 1
    print(f"{arg_count} argument{'s' if arg_count != 1 else ''}{':' if arg_count else '.'}")
    for i, arg in enumerate(argv[1:], 1):
        print(f"{i}: {arg}")
