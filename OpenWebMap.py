#!python3
#OpenMap.py - Use the default browser Launches a map

import webbrowser as WEB
import sys

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
