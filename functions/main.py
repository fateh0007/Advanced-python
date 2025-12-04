import math

def power(base,exponent):
    return base ** exponent

def multiply(a,b):
    return a*b

def area_and_perimeter_of_circle(r):
    area = math.pi * (r**2)
    perimeter = 2* math.pi * r
    return area, perimeter

num = power(4,3)
# print(num)

# print(multiply(4,6))
# print(multiply("h",6))

print(area_and_perimeter_of_circle(7.0))

cube = lambda x: x**3
print(cube(3))

def sum_all(*args):
    return sum(args)

print(sum_all(1,2,3,4,5))

#kitna bhi parameter de skte hai key value pairs ke format me inside kwargs
def print_kwaargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
print_kwaargs(name="Alice", age=30, city="New York")
print_kwaargs(fruit="Apple", color="Red")

def factorial(n):
    if n==0 or n==1 :
        return 1
    return n*factorial(n-1)

print(factorial(4))