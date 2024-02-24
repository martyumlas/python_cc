age = int(input('Enter your age: '))

if age < 2:
    print('baby')
elif age == 2 or age < 4:
    print('toddler')
elif age == 4 or age < 13:
    print('kid')
elif age == 13 or age < 20:
    print('teenager')
elif age == 20 or age < 65:
    print('adult')
else:
    print('elder')
