def classify_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid triangle sides"
    
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
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return f"{triangle_type}, right"
    
    return triangle_type
