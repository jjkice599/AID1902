import os
import re
import sys

with open('1.txt','r') as f:
    s=f.read()
  # print(s)
    l=re.split('\n\n',s)
    #MgmtEth0/RSP0/CPU0/1

    for i in range(1,len(l)-1):
        o=re.findall(r'^\S+',l[i])
        t = re.search('address is.*', l[i])
        print(o)
        print(t.group())
        print()

