# ============================================================
# PYTHON FUNCTIONS -  Python Fundamentals
# ============================================================


# ── WHAT IS A FUNCTION? ──────────────────────────────────────
# A function is a reusable block of code that performs a specific task.
# Instead of writing the same code multiple times,
# define it once and call it whenever needed.


# ── WHY USE FUNCTIONS? ───────────────────────────────────────
# - Reduces code repetition
# - Improves code organization
# - Makes programs easier to read
# - Makes code reusable
# - Simplifies debugging and maintenance


# ── SYNTAX ───────────────────────────────────────────────────

# def function_name():
#     # code

def greet():
    print("Hello")

greet()
# Output: Hello


# ── PARAMETERS AND ARGUMENTS ─────────────────────────────────

# Parameter = variable in the function definition
# Argument  = actual value passed when calling

def greet(name):        # name is a parameter
    print("Hello", name)

greet("Bhavana")        # "Bhavana" is an argument
# Output: Hello Bhavana


# ── RETURN VALUES ────────────────────────────────────────────
# return sends a value back from the function

def add(a, b):
    return a + b

result = add(10, 20)
print(result)
# Output: 30


# ── TYPE 1: No Parameters, No Return ─────────────────────────

def welcome():
    print("Welcome to Python")

welcome()
# Output: Welcome to Python


# ── TYPE 2: Parameters, No Return ────────────────────────────

def greet_user(name):
    print("Hello", name)

greet_user("Bhavana")
# Output: Hello Bhavana


# ── TYPE 3: No Parameters, Return ────────────────────────────

def get_number():
    return 10

num = get_number()
print(num)
# Output: 10


# ── TYPE 4: Parameters + Return ──────────────────────────────
# Most commonly used in real-world applications

def square(num):
    return num * num

result = square(5)
print(result)
# Output: 25


# ── SCOPE ────────────────────────────────────────────────────

# Local Scope - variable only accessible inside the function
def show():
    city = "Hyderabad"
    print(city)

show()

# Global Scope - variable accessible everywhere
country = "India"

def display():
    print(country)

display()


# ── LAMBDA FUNCTIONS ─────────────────────────────────────────
# A short one-line function

# Normal function:
def square(x):
    return x * x

# Lambda version:
square = lambda x: x * x
print(square(4))
# Output: 16


# ── REAL-WORLD USES ──────────────────────────────────────────
# Functions are used in:
# - AI and Machine Learning models
# - Automation scripts
# - Web applications
# - APIs and backend services
# - Data analysis workflows

# AI model prediction
def predict(data):
    return "Prediction based on: " + str(data)

print(predict("input_data"))

# User authentication
def authenticate(username, password):
    if username == "admin" and password == "1234":
        return True
    return False

print(authenticate("admin", "1234"))
# Output: True

# Price calculator
def calculate_total(price, tax):
    return price + (price * tax / 100)

print(calculate_total(1000, 18))
# Output: 1180.0
