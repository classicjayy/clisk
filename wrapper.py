# Clisk Python wrapper

import sys

def execute(text=None):
  if text:
    exec(f"{text}")
  else:
    print("ERROR: No text provided")

def exit():
  sys.exit(1)
