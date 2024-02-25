age = '' 

while age == '':
    try:
        age = int(input('Enter your age: '))
        if age < 3 : 
            print('Your ticket is free')
        elif age >=3 and age <= 12:
            print('Your ticket if $10')
        else: 
            print('Your ticket is $15')
    except ValueError:
        print('Invalid input')
