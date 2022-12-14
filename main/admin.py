from django.contrib import admin
from .models import Dish, Hall, Order


admin.site.register(Dish)
admin.site.register(Hall)
admin.site.register(Order)
