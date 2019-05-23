from django.db import models

# Create your models here.
class Plane(models.Model):
    name = models.CharField(max_length=200, default='Hack Plane')
    capacity = models.IntegerField()
    crew = models.IntegerField()

    def __str__(self):
        return 'Plane {name}'.format(name=self.name, unique = True)