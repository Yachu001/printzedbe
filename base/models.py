from django.db import models

# Create your models here.
class MarketingSolution(models.Model):
    title = models.CharField(max_length=200)
    tagline = models.CharField(max_length=200) 
    link = models.URLField()
    image = models.ImageField(upload_to='marketing/')

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    tagline = models.CharField(max_length=200)
    link = models.URLField()
    image = models.ImageField(upload_to='portfolio/')

    def __str__(self):
        return self.title
    
class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to='team/')

    def __str__(self):
        return self.name