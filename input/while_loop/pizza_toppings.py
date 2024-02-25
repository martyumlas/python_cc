toppings = []

is_adding_toppings = True

while is_adding_toppings:
    user_topping = input('Input your toppings ')
    if user_topping == 'done':
        is_adding_toppings = False
    else: 
        toppings.append(user_topping)
    print(f'youre toppings are {",".join(toppings)}')
