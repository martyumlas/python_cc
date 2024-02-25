person = {
    'first_name': 'michael',
    'last_name': 'Corloene',
    'age': '40',
    'city': 'new york'
}

person_1 = {
   'first_name': 'santino',
   'last_name': 'Corloene',
   'age': '40',
   'city': 'new york'
}

# for key, value in person.items():
    # print(f'{key} : {value}')

# for item in person.values():
    # print(item)

corleones = [person, person_1]

for corleone in corleones:
    print(f"{corleone['first_name'].title()} {corleone['last_name']} lives in {corleone.get('city', 'test').title()}")




