from django.contrib import admin

from .models import Employee, Meal, Lunch

admin.site.register(Employee)
admin.site.register(Meal)
admin.site.register(Lunch)
