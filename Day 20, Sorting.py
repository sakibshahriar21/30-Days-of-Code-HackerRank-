num_of_ele = int(input())

array = [int(n) for n in input().split(" ")]

num_of_swaps = 0

for i in range(num_of_ele):
    for j in range(num_of_ele - 1):
        
        if array[j] > array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp
            num_of_swaps += 1
            
    if num_of_swaps == 0:
        break
    
print('Array is sorted in ' + str(num_of_swaps) + ' swaps.')
print('First Element: ' + str(array[0]))
print('Last Element: ' + str(array[-1]))