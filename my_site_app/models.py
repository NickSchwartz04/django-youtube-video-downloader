# Create your models here.
# import the standard Django Model
# from built-in library
from django.db import models
from datetime import datetime

class homeModel(models.Model):

    # Field Names
    objects = None
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_on = models.DateTimeField(default=datetime.now)
    image = models.ImageField(upload_to="images/%Y/%m/%d")

    # rename the instances of the model
    # with their title name
    def __str__(self) -> str:
        return self.title

