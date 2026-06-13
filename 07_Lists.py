
# ==========================================
# PYTHON LISTS
# ==========================================

# LIST DEFINITION
# A list is an ordered, mutable collection
# that stores multiple items in one variable.

# ------------------------------------------
# 1. STRING LIST
# ------------------------------------------
fruits = ["Apple", "Banana", "Mango"]

# ------------------------------------------
# 2. INTEGER LIST
# ------------------------------------------
marks = [85, 90, 78, 92]

# ------------------------------------------
# 3. FLOAT LIST
# ------------------------------------------
prices = [10.5, 20.75, 30.99]

# ------------------------------------------
# 4. BOOLEAN LIST
# ------------------------------------------
status = [True, False, True]

# ------------------------------------------
# 5. MIXED LIST
# ------------------------------------------
data = ["Haseena", 21, 55.5, True]

# ------------------------------------------
# 6. EMPTY LIST
# ------------------------------------------
items = []

# ------------------------------------------
# 7. DUPLICATE VALUES LIST
# ------------------------------------------
cities = ["Mumbai", "Delhi", "Mumbai", "Chennai", "Mumbai"]

# ------------------------------------------
# 8. NESTED LIST
# ------------------------------------------
students = [
    ["Jyothi", 95],
    ["Haseena", 88],
    ["Ashwini", 91]
]

# ------------------------------------------
# 9. RANGE LIST
# ------------------------------------------
numbers = list(range(1, 11))

# ------------------------------------------
# 10. MATRIX (LIST OF LISTS)
# ------------------------------------------
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# ==========================================
# INPUT AND OUTPUT
# ==========================================

name = input("Enter your name: ")
print("Hello", name)

age = int(input("Enter your age: "))
print("Age:", age)

salary = float(input("Enter salary: "))
print("Salary:", salary)

# ==========================================
# ACCESSING ITEMS
# ==========================================

fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])     # Apple
print(fruits[1])     # Banana
print(fruits[-1])    # Mango

# ==========================================
# MODIFYING ITEMS
# ==========================================

fruits[1] = "Orange"
print(fruits)

# ==========================================
# ADDING ITEMS
# ==========================================

fruits.append("Grapes")
print(fruits)

fruits.insert(1, "Pineapple")
print(fruits)

# ==========================================
# REMOVING ITEMS
# ==========================================

fruits.remove("Orange")
print(fruits)

fruits.pop(1)
print(fruits)

# ==========================================
# LENGTH
# ==========================================

print("Length:", len(fruits))

# ==========================================
# COUNT
# ==========================================

cities = ["Mumbai", "Delhi", "Mumbai", "Chennai", "Mumbai"]
print("Mumbai Count:", cities.count("Mumbai"))

# ==========================================
# INDEX
# ==========================================

print("Delhi Index:", cities.index("Delhi"))

# ==========================================
# SORT
# ==========================================

numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)

# ==========================================
# REVERSE
# ==========================================

numbers.reverse()
print(numbers)

# ==========================================
# LOOPING THROUGH LIST
# ==========================================

for fruit in fruits:
    print(fruit)

# ==========================================
# SLICING
# ==========================================

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])

# ==========================================
# MEMBERSHIP
# ==========================================

print("Apple" in fruits)
print("Kiwi" not in fruits)

# ==========================================
# BUILT-IN FUNCTIONS
# ==========================================

marks = [85, 90, 78, 92]

print("Highest:", max(marks))
print("Lowest:", min(marks))
print("Total:", sum(marks))
print("Length:", len(marks))

# ==========================================
# COPY LIST
# ==========================================

new_marks = marks.copy()
print(new_marks)

# ==========================================
# CLEAR LIST
# ==========================================

temp = [1, 2, 3]
temp.clear()
print(temp)

# ==========================================
# JOIN LISTS
# ==========================================

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = list1 + list2
print(combined)

# ==========================================
# LIST COMPREHENSION
# ==========================================

squares = [x*x for x in range(1, 6)]
print(squares)

# ==========================================
# PRACTICE EXAMPLE
# ==========================================

food = ["Biryani", "Sambar"]

food.append("Raita")
food.append("Curd")

food.remove("Sambar")

for item in food:
    print(item)

print("Total Food Items:", len(food))
