#!/usr/bin/python3

import os
import sys
if (len(sys.argv)<=1):
 print("Add text to file by kevin agusto (addf \"text\" file)")
 sys.exit(0)

files = sys.argv[2]
text = sys.argv[1]+"\n"


if (not os.access(os.path.join(os.getcwd(), files), os.W_OK)):
 print("File doesnt exist!")
 sys.exit(0)

with open(files, "a+") as writer:
  writer.write(text)
 
 
  
