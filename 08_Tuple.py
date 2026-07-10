# ==========================================================
# PYTHON TUPLES 
# ==========================================================

# ==========================================================
# 1. WHAT IS A TUPLE?
     A tuple is an ordered, immutable (unchangeable) collection
    of items used to store multiple values in a single variable.

# Key Features:
  1. Ordered - Items maintain their order.
  2. Immutable - Items cannot be added, removed, or modified.
  3. Allows duplicate values.
  4. Supports different data types.
  ⁹5. Uses parentheses ().
# ==========================================================

fruits = ("Apple", "Banana", "Mango")
print("Tuple:", fruits)

# ==========================================================
# 2. CREATING DIFFERENT TYPES OF TUPLES
# ==========================================================

# String Tuple
colors = ("Red", "Green", "Blue")

# Integer Tuple
marks = (85, 90, 95)

# Float Tuple
prices = (10.5, 20.75, 30.99)

# Boolean Tuple
status = (True, False, True)

# Mixed Tuple
student = ("Bhavana", 21, True)

# Empty Tuple
empty_tuple = ()

# Single Item Tuple
age = (21,)

print(colors)
print(marks)
print(prices)
print(status)
print(student)
print(empty_tuple)
print(age)

# ==========================================================
# 3. ACCESSING TUPLE ELEMENTS (INDEXING)
# ==========================================================

colors = ("Red", "Green", "Blue", "Yellow")

print("First:", colors[0])
print("Second:", colors[1])
print("Fourth:", colors[3])

# ==========================================================
# 4. NEGATIVE INDEXING
# ==========================================================

fruits = ("Apple", "Banana", "Mango", "Orange")

print("Last:", fruits[-1])
print("Second Last:", fruits[-2])
print("First:", fruits[-4])

# ==========================================================
# 5. TUPLE SLICING
# ==========================================================

days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

print("First 3 Days:", days[:3])
print("Wed to Fri:", days[2:5])
print("Thu to End:", days[3:])
print("All Days:", days[:])

# ==========================================================
# 6. LOOPING THROUGH A TUPLE
# ==========================================================

animals = ("Dog", "Cat", "Tiger", "Elephant")

for animal in animals:
    print(animal)

# ==========================================================
# 7. MEMBERSHIP OPERATORS
# ==========================================================

colors = ("Red", "Green", "Blue", "Yellow")

print("Green" in colors)
print("Black" in colors)
print("Pink" not in colors)

# ==========================================================
# 8. TUPLE FUNCTIONS
# len(), count(), index()
# ==========================================================

numbers = (5, 10, 15, 10, 20, 10)

print("Length:", len(numbers))
print("Count of 10:", numbers.count(10))
print("Index of 20:", numbers.index(20))

# ==========================================================
# 9. TUPLE PACKING & UNPACKING
# ==========================================================

employee = ("Rahul", 28, "Manager")

name, age, job = employee

print("Name:", name)
print("Age:", age)
print("Job:", job)

# ==========================================================
# 10. NESTED TUPLES
# ==========================================================

books = (
    ("Python", 500),
    ("Java", 450),
    ("C++", 600)
)

print("First Book:", books[0])
print("Second Book Name:", books[1][0])
print("Third Book Price:", books[2][1])

# ==========================================================
