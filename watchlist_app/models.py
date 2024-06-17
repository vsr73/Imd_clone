from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
# class Movie(models.Model):
#     name=models.CharField(max_length=100)
#     description=models.TextField(max_length=200)
#     active=models.BooleanField(default=True)

class StreamPlatform(models.Model):
    name=models.CharField(max_length=50)
    about=models.TextField( max_length=150)
    website=models.URLField( max_length=100)
    def __str__(self):
        return self.name
    
class WatchList(models.Model):
    title=models.CharField(max_length=50)
    storyline=models.TextField( max_length=150)
    platform=models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name="watchlist")
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    # updated=models.
    def __str__(self):
        return str(self.title)


class Review(models.Model):
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description=models.CharField(max_length=200,null=True)
    created=models.DateTimeField(auto_now_add=True)
    watchlist=models.ForeignKey(WatchList,on_delete=models.CASCADE,related_name='reviews')
    active=models.BooleanField(default=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.rating)+' | '+self.watchlist.title