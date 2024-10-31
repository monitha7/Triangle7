# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classify_triangle(a,b,c):  # sourcery skip: assign-if-exp, chain-compares, reintroduce-else
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

    BEWARE: there may be a bug or two in this code
    """
    # require that the input values be >= 0 and <= 200
    if not(0<a<=200 and 0<b<=200 and 0<c<=200) or not all(isinstance(i,int) for i in (a,b,c)):
        return 'InvalidInput'
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle'
    # now we know that we have a valid triangle
    if a == b and b == c:
        return 'Equilateral'
    is_right = a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2
    if a == b or b == c or a == c:
        return 'Right Isosceles' if is_right else 'Isosceles'
    return 'Right' if is_right else 'Scalene'
