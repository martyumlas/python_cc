
try:
    number_of_guest = int(input('How many are you in the dinner group? '))
    if number_of_guest > 8: 
        print('Please wait a while')
    else:
        print('Youre table is ready')
except ValueError:
    print('Are you stupid? enter a number')
