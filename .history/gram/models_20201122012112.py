from django.db import models
from django import forms
from cloudinary.models import CloudinaryField
from . models import Profile,Comments
from tinymce.models import HTMLField
from vote.models import VoteModel
class Photo(VoteModel,models.Model):
  image = CloudinaryField('image')
  image_name = models.CharField(max_length=50)
  image_caption = models.CharField(max_length=100)
