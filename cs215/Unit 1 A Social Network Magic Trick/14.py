# cs215 ; Unit 1: A Social Network Magic Trick ; 14
import math

def time(n):
    """ Return the number of steps 
    necessary to calculate
    `print countdown(n)`"""
    steps = 0
    # YOUR CODE HERE
    return steps

def countdown(x):
    y = 0
    while x > 0:
        x = x - 5
        y = y + 1
    print y

print countdown(50)