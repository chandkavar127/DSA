# ==========================================
# 1. Positive, Negative or Zero
# ==========================================

print("----- Program 1 -----")

num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")


# ==========================================
# 2. Voting Eligibility
# ==========================================

print("\n----- Program 2 -----")

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")


# ==========================================
# 3. Largest of Three Numbers
# ==========================================

print("\n----- Program 3 -----")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest Number:", a)
elif b >= a and b >= c:
    print("Largest Number:", b)
else:
    print("Largest Number:", c)


# ==========================================
# 4. Leap Year
# ==========================================

print("\n----- Program 4 -----")

year = int(input("Enter year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


# ==========================================
# 5. Grade System
# ==========================================

print("\n----- Program 5 -----")

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Fail")


# ==========================================
# 6. Divisible by 5 and 11
# ==========================================

print("\n----- Program 6 -----")

num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("Number is divisible by 5 and 11")
else:
    print("Number is not divisible by 5 and 11")


# ==========================================
# 7. Simple Calculator
# ==========================================

print("\n----- Program 7 -----")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid Operator")
