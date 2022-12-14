
# Write a function for checking the speed of drivers. This function should have one parameter: speed.
# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
# If the driver gets more than 12 points, the function should print: “License suspended”


def speed_check(speed):
    demerit_points = 0
    excess_speed = speed - 70
    if speed < 70:
        print('Ok')
    
    while excess_speed >= 5:
        demerit_points += 1
        excess_speed -= 5

    print(f'points :{demerit_points} ')
    if demerit_points > 12:
        print('License suspended')

speed_check(130)