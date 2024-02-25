fav_number = {
    'michael': 4,
    'toto': 3,
    'amang': 2,
    'putol': 2,
    'gru': 14 
}

# fav_number = {'marites': 5}
fav_number['marites'] = 5
del fav_number['amang']
print(fav_number.get('not-existing', 'This is error excepion'))
for person, number in fav_number.items():
    print(f'{person}\'s favorite number is {number}')
