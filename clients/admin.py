from django.contrib import admin
from .models import FeaturedWorks, Review

# Register your models here.

admin.site.register(FeaturedWorks)
admin.site.register(Review)