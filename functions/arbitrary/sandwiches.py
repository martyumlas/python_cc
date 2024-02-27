def sandwich_orders(*sandwiches):
    print(f'the following orders are acknowledge: \n')
    for sandwich in sandwiches:
        print(f'{sandwich}')

sandwich_orders('egg sandwich', 'chicken sandwich', 'ham sandwich')
