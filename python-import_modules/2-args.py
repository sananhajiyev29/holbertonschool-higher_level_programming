#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    arg_count = len(argv) - 1
    if arg_count == 0:
        print("0 arguments.")
    else:
        print(f"{arg_count} argument{'s' if arg_count != 1 else ''}:")
    for i, arg in enumerate(argv[1:], 1):
        print(f"{i}: {arg}")
