'''this will return a tuple'''
def make_pizza(size, *toppings):
    print(f'{size} pizza with {",".join(toppings[:-1])} and {toppings[-1]}') 
    print(toppings)
make_pizza('large', 'pepperoni', 'mushrooms', 'green pepppers', 'extra cheese')
make_pizza('mushrooms', 'green pepppers', 'extra cheese')

def other_function_in_this_file():
    print('Hello from /arbitrary/pizza')
