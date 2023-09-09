# A py program of calculating area of triangle
#sides of a triangle

a = int(input("Enter the side a"))
b = int(input("Enter the side b"))
c = int(input("Enter the side c"))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print('The area of the triangle is', area)
