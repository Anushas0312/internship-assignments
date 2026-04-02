import re

def check_password_strength(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search("[A-Z]", password):
        return "Password must contain at least one uppercase letter."
    if not re.search("[a-z]", password):
        return "Password must contain at least one lowercase letter."
    if not re.search("[0-9]", password):
        return "Password must contain at least one digit."
    if not re.search("[@#$%^&*!]", password):
        return "Password must contain at least one special character."
    return "Strong Password ✅"

def authenticate():
    correct_password = "Admin@123"
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    print(strength)

    if password == correct_password:
        print("Authentication Successful 🎉")
    else:
        print("Authentication Failed ❌")

authenticate()