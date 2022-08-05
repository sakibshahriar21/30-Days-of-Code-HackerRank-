import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    namesList = []
    
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        
        if emailID.find('@gmail.com') != -1:
            namesList.append(firstName)
            
    for names in sorted(namesList):
        print(names)        
            