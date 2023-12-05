import re as r
import getpass as g

def passwordChecker(password):
    if not any(char.islower() for char in password):
        return 'It missing the Lowercase (weak)'
    
    if not any(char.isupper() for char in password):
        return 'It missing an Uppercase (weak)'
    
    if not any(char.isdigit() for char in password):
        return "It missing a digit (weak)"
    
    if len(password) < 8:
        return 'Too short (weak)'

    if not r.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Missing special character (weak)" 

    return 'Strong password'

while True:
    check = g.getpass(prompt='Enter your password: ')
    result = passwordChecker(check)
    print(f"The password strength: {result}")
    if result == 'Strong password':
        break


                            






