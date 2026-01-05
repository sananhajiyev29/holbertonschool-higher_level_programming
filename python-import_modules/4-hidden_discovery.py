#!/usr/bin/python3
import dis
import marshal

if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as f:
        f.read(16)  # skip header
        code_obj = marshal.load(f)
    names = sorted([name for name in code_obj.co_names if not name.startswith("__")])
    for name in names:
        print(name)
