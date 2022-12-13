from django.contrib import admin
from .models import Lot, Bid, Reviews
# Register your models here.

admin.site.register(Lot)
admin.site.register(Bid)
admin.site.register(Reviews)
