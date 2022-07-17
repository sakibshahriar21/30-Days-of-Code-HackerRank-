import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

value = 0
Max = 0

while n > 0:
    
    if n % 2 == 1:
        value += 1
        
        if value > Max:
            Max = value
            
    else:
        value = 0
        
    n //= 2

print(Max) 