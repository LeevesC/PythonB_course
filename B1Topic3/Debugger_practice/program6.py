# A program to multiply two even numbers

total = 0
number1 = int(input('Enter a number: '))
if (number1%2 == 0):
    number2 = int(input('Enter a number: '))
else:
    print('Number not even.')

if (number2%2 == 0):
    print(number1*number2);
else:
    print('Number not even.')