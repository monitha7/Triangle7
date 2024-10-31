# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3, 4, 5), 'Right', '3, 4, 5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5, 3, 4), 'Right', '5, 3, 4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1, 1, 1 should be equilateral')
    
    def testIsoscelesTriangleA(self):
        self.assertEqual(classify_triangle(2, 2, 3), 'Isosceles', '2, 2, 3 should be isosceles')
        
    def testIsoscelesTriangleB(self):
        self.assertEqual(classify_triangle(3, 2, 2), 'Isosceles', '3, 2, 2 should be isosceles')
        
    def testScaleneTriangle(self):
        self.assertEqual(classify_triangle(3, 4, 6), 'Scalene', '3, 4, 6 should be scalene')

    def testInvalidTriangleA(self):
        self.assertEqual(classify_triangle(0, 1, 2), 'InvalidInput', '0, 1, 2 should be invalid input')
    
    def testInvalidTriangleB(self):
        self.assertEqual(classify_triangle(-1, 1, 2), 'InvalidInput', '-1, 1, 2 should be invalid input')
    
    def testInvalidTriangleC(self):
        self.assertEqual(classify_triangle(1, 2, 3), 'NotATriangle', '1, 2, 3 is not a triangle')
    
    def testInvalidTriangleD(self):
        self.assertEqual(classify_triangle(1, 10, 12), 'NotATriangle', '1, 10, 12 is not a triangle')
    

