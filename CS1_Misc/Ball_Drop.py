'''
[4ex5.py]
This program calculates the total distance traveled by a ball
given a particular drop height, bounces, and bounciness.

TEST CASES:
INPUT(S)   : OUTPUTS(S)
100,5,.5   : d = 193.75 ft
25,3,.25   : d = 16.41 ft
75,7,.7    : d = 321.18 ft
42,5,.3    : d = 35.91 ft

'''

dropHeight=eval(input("Enter the Initial height in ft: "))
bounces=eval(input("Enter the number of times the ball bounces: "))
bounceIndex=eval(input("Enter Bounce Index value between 0 and 1: "))

distance = 0
while bounces > 0:

    dropHeight = dropHeight * bounceIndex
    distance = distance + dropHeight
    distance = distance + dropHeight
    bounces-=1
    
print("The total distance traveled by the ball is %.2f" % distance,"ft")

