# ==========================================
# 1. Print numbers from 1 to 10 using for loop
# ==========================================
print("----- Program 1 -----")

for i in range(1, 11):
    print(i)


# ==========================================
# 2. Print numbers from 10 to 1 using while loop
# ==========================================
print("\n----- Program 2 -----")

i = 10

while i >= 1:
    print(i)
    i -= 1


# ==========================================
# 3. Multiplication table of a number
# ==========================================
print("\n----- Program 3 -----")

num = int(input("Enter number for table: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# ==========================================
# 4. Sum of numbers from 1 to n
# ==========================================
print("\n----- Program 4 -----")

n = int(input("Enter n: "))

total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum =", total)


# ==========================================
# 5. Factorial of a number
# ==========================================
print("\n----- Program 5 -----")

n = int(input("Enter number: "))

fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)


# ==========================================
# 6. Print all even numbers between 1 and 100
# ==========================================
print("\n----- Program 6 -----")

for i in range(2, 101, 2):
    print(i)


# ==========================================
# 7. Reverse a number using a loop
# ==========================================
print("\n----- Program 7 -----")

num = int(input("Enter number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reverse =", reverse)


# ==========================================
# 8. Count the digits of a number
# ==========================================
print("\n----- Program 8 -----")

num = int(input("Enter number: "))

count = 0

while num > 0:
    num = num // 10
    count += 1

print("Number of digits =", count)


# ==========================================
# 9. Check whether a number is prime
# ==========================================
print("\n----- Program 9 -----")

num = int(input("Enter number: "))

count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not Prime Number")


# ==========================================
# 10. Fibonacci series up to n terms
# ==========================================
print("\n----- Program 10 -----")

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a)
    
    c = a + b
    a = b
    b = c
