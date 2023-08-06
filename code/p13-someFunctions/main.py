import math

def simpleFunction():
    return 10

def sumUp(a, b):
    return a + b

def rectangleArea(width, height):
    return width * height

def rectanglePerimeter(width, height):
    return (width + height) * 2

def circleArea(radius):
    return math.pi * math.pow(radius, 2)

def circumference(radius):
    return math.pi * radius * 2

width = 10
height = 5
radius = 3

print(rectanglePerimeter(width, height))
print(rectangleArea(width, height))
print(round(circleArea(radius), 2))
print(round(circumference(radius), 2))
