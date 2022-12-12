import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","Pizzeria.settings")

import django
django.setup()

from pizzas.models import *

pizzas = Pizza.objects.all()

print(pizzas)

for p in pizzas:
    print(p.pizza_name)


print('----------------------------------------')
print('Meat Lovers Pizza Toppings:')


meat_lovers = Pizza.objects.get(id=1)

toppings = Topping.objects.filter(pizza=meat_lovers)

for t in toppings:
    print(t.topping_name)

print('----------------------------------------')
print('Hawaiian Pizza Toppings:')    

hawaiian = Pizza.objects.get(id=2)

toppings = Topping.objects.filter(pizza=hawaiian)

for t in toppings:
    print(t.topping_name)


from django.contrib.auth.models import User

for user in User.objects.all():

    print(user.username)
    print(user.last_login)