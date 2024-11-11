import math
from functools import reduce

# אלגברה בסיסית 

def sum_two_numbers(a, b):
    return a + b

def sum_multiple_numbers(*args):
    return sum(args)

def subtract_two_numbers(a, b):
    return a - b

def subtract_multiple_numbers(*args):
    return args[0] - sum(args[1:])

def multiply_two_numbers(a, b):
    return a*b

def multiply_multiple_numbers(*args):
    return math.prod(args)
    # return eval('*'.join(map(str, args)))

def divide_two_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def divide_multiple_numbers(*args):
    return reduce(lambda x, y: x / y if y != 0 else (_ for _ in ()).throw(ValueError("Cannot divide by zero")), args)

def power(base, exponent):
    return base ** exponent

def square_root(number):
    return math.sqrt(number)
 

def percentage(part, whole):
    if whole == 0:
        raise ValueError("Cannot calculate percentage with a whole of zero")
    return (part / whole) * 100
  

def solve_linear_equation(a, b):
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero")
    return -b / a
  
# check basic algebra functions
print("Sum of 2 and 3:", sum_two_numbers(2, 3))
print("Sum of 1, 2, 3, 4:", sum_multiple_numbers(1, 2, 3, 4))
print("Subtract 5 from 10:", subtract_two_numbers(10, 5))
print("Subtract 1, 2, 3 from 10:", subtract_multiple_numbers(10, 1, 2, 3))
print("Multiply 2 and 3:", multiply_two_numbers(2, 3))
print("Multiply 1, 2, 3, 4:", multiply_multiple_numbers(1, 2, 3, 4))
print("Divide 10 by 2:", divide_two_numbers(10, 2))
print("Divide 100 by 2, 5, 2:", divide_multiple_numbers(100, 2, 5, 2))
print("2 to the power of 3:", power(2, 3))
print("Square root of 16:", square_root(16))
print("Percentage of 50 out of 200:", percentage(50, 200))
print("Solve linear equation 2x + 3 = 0:", solve_linear_equation(2, 3))


# גיאומטריה

def area_square(side):
    return side ** 2

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

def area_circle(radius):
    return math.pi * radius ** 2

def perimeter_square(side):
    return 4 * side

def perimeter_rectangle(length, width):
    return 2 * (length + width)

def perimeter_triangle(a, b, c):
    return a + b + c

def perimeter_circle(radius):
    return 2 * math.pi * radius

def volume_cube(side):
    return side ** 3

def volume_rectangular_prism(length, width, height):
    return length * width * height

def volume_cylinder(radius, height):
    return math.pi * radius ** 2 * height

def volume_sphere(radius):
    return (4/3) * math.pi * radius ** 3

def pythagorean_theorem(a, b):
    return math.sqrt(a ** 2 + b ** 2)

def cosine_rule(a, b, angle):
    return math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(math.radians(angle)))

# check geometry functions
print("Area of square with side 5:", area_square(5))
print("Area of rectangle with length 5 and width 3:", area_rectangle(5, 3))
print("Area of triangle with base 5 and height 3:", area_triangle(5, 3))
print("Area of circle with radius 5:", area_circle(5))
print("Perimeter of square with side 5:", perimeter_square(5))
print("Perimeter of rectangle with length 5 and width 3:", perimeter_rectangle(5, 3))
print("Perimeter of triangle with sides 5, 3, 4:", perimeter_triangle(5, 3, 4))
print("Perimeter of circle with radius 5:", perimeter_circle(5))
print("Volume of cube with side 5:", volume_cube(5))
print("Volume of rectangular prism with length 5, width 3, height 2:", volume_rectangular_prism(5, 3, 2))
print("Volume of cylinder with radius 5 and height 3:", volume_cylinder(5, 3))
print("Volume of sphere with radius 5:", volume_sphere(5))
print("Hypotenuse of right triangle with sides 3 and 4:", pythagorean_theorem(3, 4))
print("Side c of triangle with sides 3, 4 and angle 90:", cosine_rule(3, 4, 90))


# טריגונומטריה

def sine(angle):
    return math.sin(math.radians(angle))

def cosine(angle):
    return math.cos(math.radians(angle))

def tangent(angle):
    return math.tan(math.radians(angle))

# check trigonometry functions
print("Sine of 30 degrees:", sine(30))
print("Cosine of 60 degrees:", cosine(60))
print("Tangent of 45 degrees:", tangent(45))
