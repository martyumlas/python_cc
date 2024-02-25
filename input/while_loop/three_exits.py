while True:
    age = input('Enter your age :')
    try:
        if age == 'done':
            break
        elif int(age):
            age = int(age)
            if age < 3 : 
                print('Your ticket is free')
            elif age >=3 and age <= 12:
                print('Your ticket if $10')
            else: 
                print('Your ticket is $15')
    except ValueError:
        print('Invalid input')

