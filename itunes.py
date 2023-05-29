#!/usr/bin/python3
"""
"""
import request
import sys

if len(sys,argv) != 2:
    sys.exit()

response = requests.get("https://ituns.apple.com/search?entity=song&limit=term=" +sys.argv[1]

