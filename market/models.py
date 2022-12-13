import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Lot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    description = models.TextField()
    startBid = models.IntegerField(default = 1)
    image = models.ImageField(upload_to ='static/media/uploads')
    def __str__(self):
        return self.name

# implement Bid Model later
class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    amount = models.IntegerField()

class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.post.header}: {self.rating}"

# class Transaction(models.Model):
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     buyer = models.ForeignKey(User, on_delete=models.CASCADE)
#     bidAmount = models.IntegerField()