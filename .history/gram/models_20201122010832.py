from django.db import models
from django import forms
from cloudinary.models import CloudinaryField
from . models import Profile,Comments

class Photo(models.Model):
  image = CloudinaryField('image')

class ImageProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user','image','date_posted']