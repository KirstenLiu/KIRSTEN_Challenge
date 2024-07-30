# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import sys

data = sys.stdin.readlines()
num = int(data[0])  

for idx in range(num):
    card = data[idx+1]
    matched = False
    if re.match(r"^[456]\d{3}-?\d{4}-?\d{4}-?\d{4}$", card):
        matched = True
        if re.search(r"([\d])\1\1\1", card.replace("-", "")):
            #Consecutive digits are repeating 4 or more times 
            matched = False
        else:
            matched = True
    
    if matched:
        print("Valid")
    else:
        print("Invalid")
