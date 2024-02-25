from deli import sandwich_orders
from deli import finished_sandiches

sandwich_orders.extend(['pastrami', 'pastrami'])
sandwich_orders.insert(0, 'pastrami')



print('deli run out of pastrami')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current = sandwich_orders.pop()
    finished_sandiches.append(current)
    print(f'{current} is finished')

print(f'{",".join(finished_sandiches)} are ready to serve')
