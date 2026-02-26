from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

# Featured Clients
class FeaturedWorks(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='featured_works/')

    def __str__(self):
        return self.name


# Reviews
class Review(models.Model):
    SERVICE_CHOICES = [
        ('printing', 'Printing'),
        ('website', 'Website'),
        ('branding', 'Branding'),
        ('videographics', 'Video graphics'),
        ('uiux', 'Ui ux'),
    ]

    service_provided = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    rating = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    feedback = models.TextField()
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)

    primary_image = models.ImageField(upload_to='reviews/primary/')
    secondary_image = models.ImageField(upload_to='reviews/secondary/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.rating}"