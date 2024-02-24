from re import fullmatch


usernames = ['admin', 'Nikki', 'celmer', 'daniel', 'derick']

for user in usernames:
     if user == 'admin':
         print('Hello admin, would you like to see a status report?')
     else:
        print(f'Hello {user.title()}, thank you for logging again.')


current_users = [i.lower() for i in usernames[:]]
print(current_users)
new_users = ['denimar', 'marwin', 'nikki', 'Celmer']

for user in new_users:
    user_lower = user.lower()
    if user_lower in current_users:
        print(f'{user} is already used')
    else:
        print(f'{user} is available')
