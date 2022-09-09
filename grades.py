# Write a python program to input 5 subject marks and calculate total marks, percentage and grade based on following criteria
# percentage less than 50 (Grade C)
# percentage equal to 50 and less than 80 (Grade B)
# percentage equal to 80 and more than 80 (Grade A)
def gradefunc(list_marks):
    
    total = sum(list_marks)

    percentage = ( total/500 ) * 100

    if percentage < 50:
        print(" grade C")

    elif percentage < 80:
        print(" grade B")

    elif percentage >= 80:
        print(" grade A ")


gradefunc([50,60,56,58,39])