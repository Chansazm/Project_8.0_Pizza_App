specials = {'Sunday'    :   'Spinach',
            'Monday'    :   'mushroom',
            'Tuesday'   :   'pepperoni',
            'Wednesday' :   'Veggie',
            'Thursday'  :   'bbq chicken',
            'Friday'    :   'Sausage',
            'Saturday'  :   'Hawaiian'}
def order (day):
    pizza = specials[day]
    print ('order the {} pizza'.format(pizza))
