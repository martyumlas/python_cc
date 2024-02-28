def myfunction(parameter_0, parameter_1, default_param='this is default'):
    print(f'this is 1st param {parameter_0} and this is the second {parameter_1} this is the default param {default_param}')
    

def myanother_function(param1, *args, **kwargs):
    print(f'this is positional param {param1}')
    print('these are the args')

    for item in args:
        print(f'{item}')
    
    print('these are the kwargs')
    for key, value in kwargs.items():
        print(f'{key} : {value}')

# myanother_function('default', 'one', 'two', 'three', item1='this is item 1', item2='this item 2')


        
