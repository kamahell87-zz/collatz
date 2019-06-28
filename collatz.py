def collatz(numbers):
    
    #check if 'numbers' is odd or even and do the operations untill return 1
    while numbers != 1:
        if numbers % 2 == 0: #even
            numbers = (numbers // 2)
            print(numbers)
        elif numbers % 2 == 1: #odd
            numbers = (3 * numbers + 1)
            print(numbers)
        continue

while True:
    
    #only integers in 'numbers', nothing else
    try:
        numbers = int(input('Please, enter a number: '))
        print(collatz(numbers))
    except ValueError:
        print('Sorry, I meant an integer.')
