from django.db import models

# Create your models here.
class Lot(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    startBid = models.IntegerField(default = 1)
    # add image field later

    def __str__(self):
        return self.name

# implement Bid Model later
