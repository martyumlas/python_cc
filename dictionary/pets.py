from typing import cast


dog = {
    'name': 'bantay',
    'owner': 'toto',
    'breed': 'askal'
}

cat = {
    'name': 'muning',
    'owner': 'dorobo',
    'breed': 'pusang kalye'
}

hamster = {
    'name': 'dodie',
    'owner': 'mario',
    'breed': 'dagang kosta'
}

pets = [dog, cat, hamster]


for pet in pets:
    print(f'name: {pet["name"]}')
    print(f'owner: {pet["owner"]}\n')










