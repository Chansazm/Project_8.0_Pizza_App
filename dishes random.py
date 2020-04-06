"""Scrubbing a Stubbon pan"""

import random

dirty = True
scrub_count = 0

while dirty == True:

    scrub_count += 1
    print('Scrub the pan: {}'.format(scrub_count))

    print ('Rinse and check if the pan is clean')

    if not random.randint(0,9):
        print('All clean')
        dirty = False
    else:
        print('Still dirty...')
