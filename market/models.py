from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Lot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    description = models.TextField()
    startBid = models.IntegerField(default = 1)
    image = models.ImageField(upload_to ='static/media/uploads')
    # add image field later

    def __str__(self):
        return self.name

# implement Bid Model later
