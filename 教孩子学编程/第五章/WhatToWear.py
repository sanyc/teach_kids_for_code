rainy = input('How\'s the weather? Is is raining? (y/n)').lower()
cold = input('Is it cold outside? (y/n)').lower()
if rainy == 'y' and cold == 'y':
    print('You\'d better wear a raincoat.')
elif rainy == 'y' and cold != 'y':
    print('Carry an umbrella with you.')
elif rainy != 'y' and cold == 'y':
    print('Put on a jacket, it\'s cold out!')
elif rainy != 'y' and cold != 'y':
    print('Wear whatecer you want, it\'s beautiul outside!')