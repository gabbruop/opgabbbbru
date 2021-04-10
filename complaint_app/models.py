from django.db import models

# Create your models here.

class complaint(models.Model):
    username = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    complaint = models.TextField()
    date = models.DateField(null=True)

class reply(models.Model):
    username = models.CharField(max_length=150)
    complaint_id = models.IntegerField()
    reply = models.TextField()
    userstatus = models.CharField(max_length=150, default='user')
    date = models.DateField(null=True)