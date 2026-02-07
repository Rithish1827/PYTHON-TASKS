password=input("Enter your password: ")
def valid_pass(password):
    for i in password:
        if len(password)<8:
            return "Password must be at least 8 characters long."
        elif not any(char.isdigit() for char in password):
            return "Password must contain at least one digit."
        elif not any(char.isupper() for char in password):
            return "Password must contain at least one uppercase letter."
        elif not any(char.islower() for char in password):
            return "Password must contain at least one lowercase letter."
        elif not any(char in "!@#$%^&*()-+" for char in password):
            return "Password must contain at least one special character (!@#$%^&*()-+)."
validation_result = valid_pass(password)
print(validation_result)

