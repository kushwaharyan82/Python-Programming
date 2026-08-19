# 41. Calculate Simple Interest
P = float(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))

SI = (P * R * T) / 100

print("Simple Interest:", SI)


# 42. Area of Rectangle
L = float(input("Enter length: "))
B = float(input("Enter breadth: "))

area = L * B

print("Area:", area)


# 43. Area of Triangle
B = float(input("Enter base: "))
H = float(input("Enter height: "))

area = 0.5 * B * H

print("Area:", area)


# 44. Area of Circle
PI = 3.14

r = float(input("Enter radius: "))

area = PI * r ** 2

print("Area:", area)


# 45. Circumference of Circle
PI = 3.14

r = float(input("Enter radius: "))

circumference = 2 * PI * r

print("Circumference:", circumference)


# 46. Celsius to Fahrenheit
C = float(input("Enter Celsius: "))

F = C * 9 / 5 + 32

print("Fahrenheit:", F)


# 47. Fahrenheit to Celsius
F = float(input("Enter Fahrenheit: "))

C = (F - 32) * 5 / 9

print("Celsius:", C)


# 48. Meters to Kilometers
meters = float(input("Enter meters: "))

kilometers = meters / 1000

print("Kilometers:", kilometers)


# 49. Volume of Cube
side = float(input("Enter side: "))

volume = side ** 3

print("Volume:", volume)


# 50. Swap two numbers using a temporary variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)
