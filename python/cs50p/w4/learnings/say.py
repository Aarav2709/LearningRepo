import sys  # Take in-line input.

from sayings import hello  # Import our own library (sayings.py)!

if len(sys.argv) == 2:
    hello(sys.argv[1])
