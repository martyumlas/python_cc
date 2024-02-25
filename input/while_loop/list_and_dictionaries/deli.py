sandwich_orders = ['chicken sandwich', 'breakfast sandwich', 'reuben sandwich', 'vegetable sandwich']
finished_sandiches = []

if __name__ == "__main__":
    while sandwich_orders:
        current_order = sandwich_orders.pop()
        print(f'{current_order} is finished')
        finished_sandiches.append(current_order)
    print(f'\nthe following orders are finished')

    for sandwich in finished_sandiches:
        print(f'{sandwich}')
