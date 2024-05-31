from django.db import models

# Create your models here.
class contactform(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    subject = models.CharField(max_length=300)
    message = models.TextField(blank=True)
    mobile = models.IntegerField(blank=True)
    def __str__(self):
        return self.name