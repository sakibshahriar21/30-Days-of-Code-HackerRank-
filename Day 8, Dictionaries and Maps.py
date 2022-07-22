# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

n = int(input())
phone_Book = {}

for i in range(n):
    entry = input().split(' ')
    phone_Book[entry[0]] = entry[1]
    
query = sys.stdin.readlines()

for i in query:
    name = i.strip()
    if name in phone_Book:
        print(name + '=' + str( phone_Book[name] ))
    else:
        print('Not found')