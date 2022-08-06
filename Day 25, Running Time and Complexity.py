from math import sqrt
from sys import stdin

def checkPrime(value):
    for i in range(2, int(sqrt(value))+1):
        if value % i == 0:
            return False
    return True

n = int(input())

for i in stdin:
    value = int(i)
    
    if value >= 2 and checkPrime(value):
        print('Prime')
    else:
        print('Not prime')