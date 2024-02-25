available_cars = ['subaru', 'honda', 'toyota']

# car = input('What car would you like to rent? ')

for k, v in enumerate(available_cars, start=1):
    print(f"{k}. {v}")

chosen_car = ''

while chosen_car == '':
    try:
        choice = int(input('Enter the car you want to rent:  '))
        if choice <= len(available_cars):
            chosen_car = available_cars[choice - 1]
            print(f'You have chosen {chosen_car}')
        else:
            print('Invalid input')
    except ValueError:
        print('Invalid input. Please enter a number')
        
