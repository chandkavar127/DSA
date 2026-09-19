# ==========================================
# 1. Demonstrate Data Types
# ==========================================

a = 10
b = 10.5
c = "Chand"
d = True
e = 2 + 3j

print("----- Program 1 -----")
print("Integer:", a, type(a))
print("Float:", b, type(b))
print("String:", c, type(c))
print("Boolean:", d, type(d))
print("Complex:", e, type(e))


# ==========================================
# 2. Accept two numbers and display types
# ==========================================

print("\n----- Program 2 -----")

num1 = int(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("First number:", num1)
print("Type:", type(num1))

print("Second number:", num2)
print("Type:", type(num2))


# ==========================================
# 3. Convert String into Integer and Float
# ==========================================

print("\n----- Program 3 -----")

x = "100"

integer_value = int(x)
float_value = float(x)

print("String:", x)
print("Integer:", integer_value)
print("Float:", float_value)


# ==========================================
# 4. Find Length of String
# ==========================================

print("\n----- Program 4 -----")

name = "Chand Kavar"

print("String:", name)
print("Length:", len(name))


# ==========================================
# 5. List, Tuple, Set and Dictionary
# ==========================================

print("\n----- Program 5 -----")

my_list = [10, 20, 30]
my_tuple = (10, 20, 30)
my_set = {10, 20, 30}
my_dictionary = {"name": "Chand", "age": 22}

print("List:", my_list)
print("Type:", type(my_list))

print("Tuple:", my_tuple)
print("Type:", type(my_tuple))

print("Set:", my_set)
print("Type:", type(my_set))

print("Dictionary:", my_dictionary)
print("Type:", type(my_dictionary))
