import sys
b = 1000
def depositFunction():
    global b
    user = int(input('enter the amonut to be deposit'))
    b += user
    print(f'the amount {user} is deposited')

def withDrawMoney():
    global b
    while True:
        
        user = int(input('enter the amount to withdraw'))        
        if user.isdigit():
            return 'Please input a number'
        if user <= b or user >= b:
            return 'insufficent amount'
        if user == 1000 or user == 100000:
            return 'reach the limit'
        else:
            b -= user
            print(f'The amount {user} is withdrawed')
            
def checkBalance():
    return f'{b}'

    
while True:
    print('1. Deposit money \t 2. Withdraw \t 3. Check balance \t 4. Exit')
    option = int(input('Choose your mode: '))
    
    if option == 1:
        result = depositFunction()  # Capture the return value
        print(result)  # Display the result
        
    elif option == 2:
        result = withDrawMoney()  # Capture the return value
        print(result)  # Display the result

    elif option == 3:
        result = checkBalance()  # Capture the return value
        print(result)  # Display the result

    elif option == 4:
        sys.exit()

    else:
        print('Invalid mode chosen. Please choose a valid option.')
