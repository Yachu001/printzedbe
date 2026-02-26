from django.db import models

# Create your models here.

# Core Service
class CoreService(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='core_services/')

    def __str__(self):
        return self.title


# We Provide
class WeProvide(models.Model):
    index = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='we_provide/')

    def __str__(self):
        return f"{self.index} - {self.title}"