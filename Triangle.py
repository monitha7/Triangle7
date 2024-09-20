def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid triangle sides"
    #test comment
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"
    
    if a == b == c:
        triangle_type = "equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "isosceles"
    else:
        triangle_type = "scalene"
    
    # Check for right triangle
    sides = sorted([a, b, c])
    if round(a**2 + b**2, 5) == round(c**2, 5) or round(b**2 + c**2, 5) == round(a**2, 5) or round(a**2 + c**2, 5) == round(b**2, 5):
        return f"{triangle_type}, right"
    
    return triangle_type
