import sys

b = 1000

def depositFunction():
    global b
    try:
        user = int(input('Enter the amount to deposit: '))
        if user <= 0:
            return 'Please enter a valid positive amount'
        b += user
        return f'Deposited {user} successfully. New balance: {b}'
    except ValueError:
        return 'Please input a valid number'

def withDrawMoney():
    global b
    while True:
        try:
            user = int(input('Enter the amount to withdraw: '))
        except ValueError:
            return 'Please input a valid number'
        
        if user <= 0:
            return 'Please enter a valid positive amount'
        
        if user > b:
            return 'Insufficient balance'
        
        if user % 1000 != 0 and user != 100000:
            return 'Amount must be a multiple of 1000 or 100000'
        
        b -= user
        return f'Withdrawn {user} successfully. New balance: {b}'

def checkBalance():
    return f'Your balance is: {b}'

while True:
    print('1. Deposit money \t 2. Withdraw \t 3. Check balance \t 4. Exit')
    option = int(input('Choose your mode: '))
    
    if option == 1:
        result = depositFunction()  # Capture the return value
        print(result)  # Display the result
        
    elif option == 2:
        result = withDrawMoney()  # Capture the return value
        if result == 'Insufficient balance':
            print(result)
            break  # Exit the withdrawal loop on insufficient balance
        print(result)  # Display the result

    elif option == 3:
        result = checkBalance()  # Capture the return value
        print(result)  # Display the result

    elif option == 4:
        sys.exit()

    else:
        print('Invalid mode chosen. Please choose a valid option.')
