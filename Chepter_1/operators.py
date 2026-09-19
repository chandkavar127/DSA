# ==========================================
# 1. Addition, Subtraction, Multiplication, Division
# ==========================================

a = 20
b = 5

print("----- Program 1 -----")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


# ==========================================
# 2. Remainder and Quotient
# ==========================================

print("\n----- Program 2 -----")

a = 17
b = 5

print("Remainder:", a % b)
print("Quotient:", a // b)


# ==========================================
# 3. Even or Odd
# ==========================================

print("\n----- Program 3 -----")

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# ==========================================
# 4. Relational Operators
# ==========================================

print("\n----- Program 4 -----")

a = 10
b = 20

print("a > b :", a > b)
print("a < b :", a < b)
print("a == b:", a == b)
print("a != b:", a != b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


# ==========================================
# 5. Logical Operators
# ==========================================

print("\n----- Program 5 -----")

a = 10
b = 20

print("AND:", a > 5 and b > 15)
print("OR :", a > 15 or b > 15)
print("NOT:", not(a > 5))


# ==========================================
# 6. Assignment Operators
# ==========================================

print("\n----- Program 6 -----")

x = 10

x += 5
print("After += 5:", x)

x -= 2
print("After -= 2:", x)

x *= 2
print("After *= 2:", x)

x /= 2
print("After /= 2:", x)


# ==========================================
# 7. Largest of Two Numbers
# ==========================================

print("\n----- Program 7 -----")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest Number:", a)
elif b > a:
    print("Largest Number:", b)
else:
    print("Both numbers are equal")
