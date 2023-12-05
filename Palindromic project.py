def checkPalindromic(number):
    string = str(number)  # Convert the number to a string
    reversed_string = string[::-1]  # Reverse the entire string
    if string == reversed_string:
        print('True')
    else:
        print('False')

def checkReverseString(word):
    reversed_word = word[::-1]  # Reverse the word
    if word == reversed_word:
        print('True')
    else:
        print('False') 

def stringcheck():
    while True:
        print('Enter a word less than 10 alphabets')
        word = input('Enter the word: ')
        if word.isalpha() and len(word) < 10:
            checkReverseString(word)
            break
        else:
            print("It's not a valid word.")

def numberCheck():
    while True:
        digit = input('Enter a number for check: ')
        if digit.isdigit():
            checkPalindromic(digit)
            break
        else:
            print("Not a digit. Please enter a valid number.")

def ShowreverseString():
    while True:
        string = input('enter the word ')
        if string.isalpha() and len(string) < 10:
            digit = string[::-1]
            print(digit)
        else :
            print('its not a valid')
            break



while True:
    print('1. Check number')
    print('2. Check word')
    print('3.show reverse word')
    nlp = input("Choose the mode: ")
    if nlp.isdigit():
        nlp = int(nlp)
        if nlp == 1:
            numberCheck()
        elif nlp == 2:
            stringcheck()
        elif nlp == 3:
            ShowreverseString()
        else:
            print('Invalid mode.')
    else:
        print('Invalid input. Please enter 1 or 2 to choose the mode.')
