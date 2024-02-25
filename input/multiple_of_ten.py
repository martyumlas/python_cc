num = '' 
while num == '':
    try:
        num = int(input('Enter a number '))
        if num % 10 == 0:
            print(f'{num} is multiple of ten')
        else:
            print(f'{num} is not multiple of ten')
    except ValueError:
        print('Please enter a number')
