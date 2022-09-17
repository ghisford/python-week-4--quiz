
# Write a program which will find all such numbers which are divisible by 7 but are 
# not a multiple of 5 between 2000 and 3200 (both included). 
# The numbers obtained should be printed in a comma-separated sequence on a single line.
import math
def multiples_of_7():
    num_list  = []
    first_divisible =( math.ceil(2000/7))*7
    
    for i in range(first_divisible,3201,7):
        if i % 5 != 0:
            print(i,end=",")
            
multiples_of_7()
