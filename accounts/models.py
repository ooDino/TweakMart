from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bal = models.IntegerField(blank=True, null=True, default = 0)
    phone_number = models.PositiveBigIntegerField(blank=True, null=True, default=0)
    address = models.CharField(blank='', max_length=100, default='0')
    card_number = models.PositiveBigIntegerField(blank=True, null=True, default=0)
    card_name = models.CharField(blank='', max_length=100, default=0)
    expire = models.CharField(blank='', max_length=10, default='0')
    cvv = models.PositiveBigIntegerField(blank=True, null=True,default=0)   
    # add more fields as needed

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()