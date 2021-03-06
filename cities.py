cities = {'Брянск': {'Страна': 'Россия', 'Население': '400.000', 'Интересный факт': 'Брянск - один из самых старых городов России и это мой родной город'},
'Москва': {'Страна': 'Россия', 'Население': '13.000.000', 'Интересный факт': 'Москва - столица России'}, 'Санкт-Петербург': {'Страна': 'Россия', 'Население': '5.000.000',
'Интересный факт': 'Санкт-Петербург - это "северная столица России" и "город белых ночей"'}, 'Трубчевск': {'Страна': 'Россия', 'Население': '14.000',
'Интересный факт': 'Трубчевск - один из древнейших городов Брянской области, на десять лет старше областного центра, которым является Брянск.'}}
for city, city_description in cities.items():
    print(f'\nГород: {city}')
    country = city_description['Страна']
    print(f'\tСтрана: {country}')
    population = city_description['Население']
    print(f'\tНаселение: {population}')
    fact = city_description['Интересный факт']
    print(f'\tИнтересный факт: {fact}')
