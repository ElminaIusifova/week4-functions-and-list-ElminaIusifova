def function():
    a= int(input("Enter your first number: "))
    b= int(input("Enter your second number: "))
    if a > b:
        return a
    return b

print(f"Your maximum number is: {function()}")
