"""Putting away clean dishes"""

import random

dishwasher = ['plate','bowl','cup','knife','fork','spoon','plate','spoon','bowl','cup','knife','cup','cup','fork','plate','cup','spoon','knife']

for dish in list (dishwasher):

    if not random.randint(0,19):
        print('Out of space')
        break
    else:
        print('putting {} in the cabinet'.format(dish))
        dishwasher.remove(dish)
