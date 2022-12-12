from django.contrib import admin

# Register your models here.

from .models import *
from .models import Pizza
from .models import Topping

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Comment)