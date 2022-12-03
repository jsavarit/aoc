import sys
from importlib import import_module

def run(func, filename):
    with open(filename) as f:
        print(func(f))

d = sys.argv[1]
module = import_module(f"py.day{d}")

for i in ("p1", "p2"):
    run(getattr(module, i), f"input/day{d}.txt")