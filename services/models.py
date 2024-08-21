from django.db import models

# Create your models here.
class Services(models.Model):
    service = models.CharField(max_length=100)

    def __str__(self):
        return self.service()

class Description(models.Model):
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.description()

class About(models.Model):
    information = models.CharField(max_length=1000)

    def __str__(self):
        return self.information()



