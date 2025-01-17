# from math import cos
import math
def calc(a,b,operator):
    if operator == '+':
        return b+math.cos(a)
    elif operator == '-':
        return a-b
    elif operator == '*':
        return a*b