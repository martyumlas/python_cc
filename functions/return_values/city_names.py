def city_country(city, country):
    return f'{city.title()}, {country.upper() if country.isupper() else country.title()}'

print(city_country('manila', 'philippines'))
print(city_country('new york', 'USA'))
print(city_country('london', 'UK'))
