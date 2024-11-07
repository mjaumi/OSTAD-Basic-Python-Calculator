print('Welcome to Basic Calculator Project!!')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')

option = int(input('Select an Option for Basic Calculator Operation: '))

if option == 1:
    num1 = int(input('Enter 1st Number: '))
    num2 = int(input('Enter 2nd Number: '))

    add = num1 + num2
    print('Addition of {} and {} is: {}'.format(num1, num2, add))

elif option == 2:
    num1 = int(input('Enter 1st Number: '))
    num2 = int(input('Enter 2nd Number: '))

    sub = num1 - num2
    print('Subtraction of {} and {} is: {}'.format(num1, num2, sub))

elif option == 3:
    num1 = int(input('Enter 1st Number: '))
    num2 = int(input('Enter 2nd Number: '))

    mul = num1 * num2
    print('Multiplication of {} and {} is: {}'.format(num1, num2, mul))

elif option == 4:
    num1 = int(input('Enter 1st Number: '))
    num2 = int(input('Enter 2nd Number: '))

    div = num1 / num2
    print('Division of {} and {} is: {}'.format(num1, num2, div))

else :
    print('Invalid Option!!')

