# Write a python program to sort array element in the ascending/descending order
def sorterfunc(d):
    i = 0
    j = 0
    lenght = (len(d)-1)
    while j < lenght:
        while i < lenght:
            if d[i] > d[i+1]:
                d[i+1],d[i] = d[i],d[i+1]
            i = i + 1
    j = j+1
    return d

print(sorterfunc([6,1,7,2]))

# 
# Write a function for checking the speed of drivers. This function should have one parameter: speed.
# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
# If the driver gets more than 12 points, the function should print: “License suspended”
# Write a function called show_stars(rows). If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5 between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
# Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H] Following are the fixed values of C and H: C is 50. H is 30. D is the variable whose values should be input to your program in a comma-separated sequence. Example Let us assume the following comma separated input sequence is given to the program: 100,150,180 The output of the program should be: 18,22,24

# Write a function to compute 5/0 and use try/except to catch the exceptions.

# Create a nesting list that prints out the color and the car brand.

# Bonus Question: Algorithm challenge: Create your own sorting algorithm.