class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def  computeDifference(self):
        Max = 0
        
        for i in range(len(self.__elements)):
            for j in range(len(self.__elements)):
                
                absolute = abs(self.__elements[i] - self.__elements[j])
                
                if absolute > Max:
                    Max = absolute
                    
        self.maximumDifference = Max            

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)