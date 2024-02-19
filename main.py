
#Defining Fuctions for each operation
def Addition(a, b):
    return a + b

def Subtraction(a , b):
    return a-b

def Multiplication (a,b):
    return a*b

def Division(a,b) :
   return 'Error:Cannot perform operation: Division by zero' if b==0 else a /b

if __name__ =="__main__": # Runs within the module and cannot be run when imported
    # Print a welcome message
    print('Welcome to the My Calculator App!')

    # Main loop for user interaction
    while True:
        # Display menu options to the user
        print('\nChoose the Operator Accordingly!!!')
        print('**********************')
        print('+ . To perform Addition')
        print('- . To perform Subtraction')
        print('* . To perform Multiplication')
        print('/ . To perform Division')
        print('Q. Quit')

        # Prompt the user to enter their choice
        users_input = input('Please choose your desired operation: ')
        number1=float(input('Enter your first number: '))
        number2=float(input('Enter your second number: '))

        # Process user input based on the chosen option
        if (users_input=='+'):
            print(f'The Addition of {number1} and {number2}  is: ', Addition(number1,number2))
        elif (users_input=='-'):
            print(f'The subtraction of {number1} and {number2}  is: ', Subtraction(number1,number2))
        elif(users_input=='*'):
            print(f'The Multiplication of {number1} and {number2}  is: ', Multiplication(number1,number2))
        elif(users_input=='/'):
            print(f'The Division of {number1} and {number2}  is: ', Division(number1,number2))
        elif(users_input=='Q'):
            # Exit the program if the user chooses to quit
            break
        else:
            # Print an error message for invalid input
            print('The Input choice is invalid. Please Try Again later! 😟')

    # Print a farewell message when the program exits
    print('Thank you for using my calculator App!!! 🙋‍♂️🙋‍♂️🙋‍♂️')
