import os, sys
try:
    __import__("spy").Main()
except Exception as e:
    exit(str(e))
