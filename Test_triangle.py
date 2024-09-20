import unittest
from Triangle import classify_triangle

#Test comment
class TestClassifyTriangle(unittest.TestCase):

    def test_equilateral(self):
        self.assertEqual(classify_triangle(1, 1, 1), "equilateral")
    
    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 8), "isosceles")
        self.assertEqual(classify_triangle(7, 7, 5), "isosceles")

    def test_scalene(self):
        self.assertEqual(classify_triangle(2, 3, 4), "scalene")
    
    def test_right_triangle(self):
        self.assertEqual(classify_triangle(8, 6, 10), "scalene right triangle")
        self.assertEqual(classify_triangle(9, 12, 15), "scalene right triangle")

    def test_isosceles_right_triangle(self):
        self.assertEqual(classify_triangle(1, 1, (2 ** 0.5)), "isosceles right triangle")

    def test_invalid_triangle(self):
        self.assertEqual(classify_triangle(-1, 2, 2), "Invalid triangle")
        self.assertEqual(classify_triangle(1, 1, 2), "Invalid triangle")
        self.assertEqual(classify_triangle(0, 5, 5), "Invalid triangle")
        self.assertEqual(classify_triangle(5, 5, 10), "Invalid triangle")

if __name__ == '__main__':
    unittest.main()
