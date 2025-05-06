# Basic Python Code Example

# 1. Variables and Data Types
name = "Alice"
age = 25
height = 5.4
is_student = True

# 2. Conditional Statement
if is_student:
    print(f"{name} is a student.")
else:
    print(f"{name} is not a student.")

# 3. Loop (for)
for i in range(1, 6):
    print(f"Counting: {i}")

# 4. Function
def greet(person_name):
    return f"Hello, {person_name}!"

# Calling the function
print(greet(name))

# 5. Getting User Input
user_name = input("Enter your name: ")
print("Welcome,", user_name)
