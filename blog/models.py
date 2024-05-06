from django.db import models

class service(models.Model):

    service_icon = models.CharField(max_length=40)
    service_title = models.CharField(max_length=40)
    service_des = models.TextField()

class skills(models.Model):
    skill_icon = models.CharField(max_length=50)
    skill_icon_style = models.CharField(max_length=50)
    skill_title = models.CharField(max_length=50)

class Contact_Me(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    msg = models.TextField(max_length=400)
