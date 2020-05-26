#!/usr/bin/env python
# coding: utf-8



import re
import sys 
import os
def sed(firstStr, secondStr, file):
    if not os.path.exists(file):
        print("Provided file",file,"not exist")
        return 1
    with open(file, "r") as sources:
        lines = sources.readlines()
    
    reg=r""+ firstStr
    with open(file, "w") as sources:
        for line in lines:
            # print(re.sub(reg, secondStr, line))
            sources.write(re.sub(reg, secondStr, line))




n = len(sys.argv)
print(sys.argv)
if n!=4:
	print("You have provided invalid number of arguments (Expecting 3)")
else:
    pattrn=sys.argv[1]
    replacement=sys.argv[2]
    file=sys.argv[3]
    sed(pattrn,replacement,file)





