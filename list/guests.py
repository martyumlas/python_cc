guests = ['michael', 'marlon', 'jackie', 'ruben']

for guest in guests:
    print(f'Hi {guest.title()} I\'m inviting you to dinner')

guest_who_cant_make_it = ['michael', 'marlon']
unpack_guest_who_cant_make_it = ', '.join(guest_who_cant_make_it).title()
addtional_guests = ['jordan', 'kobe']
addtional_guests.append('horry')
guests.extend(addtional_guests)

for guest in guests[:]:
    if guest in guest_who_cant_make_it:
        guests.remove(guest)
        print(f'{guest.title()} can\'t come')
    elif guest in addtional_guests:
        print(f'{guest.title()} you are now invited')
    else:
        print(f'{guest.title()} you are still invited')


while(len(guests) > 2):
    unvinted = guests.pop()
    print(f'Sorry {unvinted.title()} I cant invite you anymore')

