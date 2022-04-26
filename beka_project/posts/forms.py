from django import forms
from .models import *
class PostCreate(forms.ModelForm):
    class Meta:
            model = Posts
            fields = '__all__'

GChoices = (('M', 'Male'), ('F', 'Female'),)

class CreateUser(forms.ModelForm):
    class Meta:
        model = RegUser
        fields = "__all__"