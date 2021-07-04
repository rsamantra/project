from django.db import models

class Item(models.Model):
    STATUS = [
        ("pending","PENDING"),
        ("Completed","COMPLETED")
    ]
    item = models.CharField(max_length=200)
    status = models.CharField(STATUS, default="pending",max_length=100)
