from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()

    def __str__(self):
        return self.first_name
