from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator

class Actor(models.Model):
    title=models.CharField(max_length=255)
    def __str__(self):
        return self.title
class Table(models.Model):
    title=models.CharField(max_length=255)
    picture=models.ImageField(default='default value')
    content=models.TextField(blank=True)
    def __str__(self):
        return self.title
class Posts(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField(blank=True)
    picture=models.ImageField(default='default value')
    author=models.CharField(max_length=30, default='anonymous')
    email=models.EmailField(blank=True)
    describe=models.TextField(default=' DataFlair Django tutorial')
    def __str__(self):
        return self.title
class RegUser(models.Model):
    firstname = models.CharField(max_length=255, verbose_name="First name")
    lastname = models.CharField(max_length=255, verbose_name="Last name")
    user_id = models.PositiveIntegerField(primary_key=True, default=1)
    GChoices = (('M', 'Male'), ('F', 'Female'),)
    gender = models.CharField(max_length=1, choices=GChoices)
    email = models.EmailField(validators=[MinLengthValidator(10)])
    username = models.CharField(max_length=255, verbose_name="Username")
    password = models.CharField(max_length=255)
# Create your models here.
