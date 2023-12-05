import math as m
def areaOfcircle(radius):
    area = m.pi * radius **2
    print(f"The area of circle {area}")

print('Enter the radius of the cirlce')
user = input()
circleArea = areaOfcircle(int(user))
print(f"the area of circle is :  {circleArea}")

    