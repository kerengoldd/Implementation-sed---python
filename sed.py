#!/usr/bin/env python
# coding: utf-8



import re
import sys 
import os
def sed(firstStr, secondStr, file):
    if not os.path.exists(file):
        print("Provided file",file," does not exist.")
        print("Usage1: python",sys.argv[0],"-f","\"pattern\"","\"replacement\"","file")
        print("Usage2: python",sys.argv[0],"\"pattern\"","\"replacement\"","\"string\"")
        return 1
    with open(file, "r") as sources:
        lines = sources.readlines()
        #print(lines)
    
    reg=r""+ firstStr
    #print(reg)
    with open(file, "w") as sources:
        for line in lines:
            # print(re.sub(reg, secondStr, line))
            sources.write(re.sub(reg, secondStr, line))



n = len(sys.argv)

#works on file
if n==4:
    pattrn=sys.argv[1]
    replacement=sys.argv[2]
    string=sys.argv[3]
    reg=r""+ pattrn
    print(re.sub(reg, replacement, string))

#works on string    
elif n==5 and sys.argv[1]=="-f":
    pattrn=sys.argv[2]
    replacement=sys.argv[3]
    file=sys.argv[4]
    sed(pattrn,replacement,file)
    
else:
    print("You have provided invalid number of arguments")
    print("Usage1: python",sys.argv[0],"-f","\"pattern\"","\"replacement\"","file")
    print("Usage2: python",sys.argv[0],"\"pattern\"","\"replacement\"","\"string\"")
    





