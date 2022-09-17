# Write a function called show_stars(rows). If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****

def show_stars(rows):
    star = '*'
    for i in range(1,rows +1):
        print(star * i)
    

show_stars(5)