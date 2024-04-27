from django.db import models

# Create your models here.

#CRUD => Create Read Update Delete

class student (models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField()


class car(models.Model):
    car_name=models.CharField(max_length=20)
    speed=models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.car_name
