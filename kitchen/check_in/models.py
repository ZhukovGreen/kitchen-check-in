from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=64)

    def __str__(self):
        return self.full_name


class Meal(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=512)

    def __str__(self):
        return f'{self.name} ({self.description[:24]}...)'


class Lunch(models.Model):
    employee = models.ForeignKey(to=Employee, on_delete=models.CASCADE)
    meal = models.ForeignKey(to=Meal, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.employee} ate {self.meal.name} on {self.date}'
