# ==========================================
# 1. Function to print Hello World
# ==========================================
def hello():
    print("Hello, World!")
hello()

# ==========================================
# 2. Function that takes name and prints greeting
# ==========================================
def greet(name):
    print("Hello", name)
greet("Chand")

# ==========================================
# 3. Function to add two numbers
# ==========================================
def add(a, b):
    return a + b
print("Addition:", add(10, 20))

# ==========================================
# 4. Function to find square of a number
# ==========================================
def square(n):
    return n * n
print("Square:", square(5))

# ==========================================
# 5. Function to check even or odd
# ==========================================
def even_odd(n):
    if n % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")
even_odd(10)

# ==========================================
# 6. Function to find maximum of two numbers
# ==========================================
def maximum(a, b):
    if a > b:
        return a
    else:
        return b
print("Maximum:", maximum(10, 20))

# ==========================================
# 7. Celsius to Fahrenheit
# ==========================================
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32
print("Fahrenheit:", celsius_to_fahrenheit(30))

# ==========================================
# 8. Area of a Circle
# ==========================================
def circle_area(radius):
    return 3.14 * radius * radius
print("Circle Area:", circle_area(5))

# ==========================================
# 9. Factorial of a number
# ==========================================
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
print("Factorial:", factorial(5))

# ==========================================
# 10. Positive, Negative or Zero
# ==========================================
def check_number(n):
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")
check_number(-5)
