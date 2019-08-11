from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django import forms
from MEC import settings
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail

class Board(models.Model):
    idx = models.AutoField(primary_key=True)
    writer = models.CharField(null=False, max_length=50)
    title = models.CharField(null=False, max_length=120)
    hit = models.IntegerField(default=0)
    content = models.TextField(null=False)
    post_date = models.DateTimeField(default=datetime.now, blank=True)
    filename = models.CharField(null=True, blank=True, default="", max_length=500)
    filesize = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    ratings_up = models.IntegerField(default=0)
    ratings_down = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
                                      
    def hit_up(self):
        self.hit += 1
    def down_up(self):
        self.down += 1
    def rate_up(self):
        self.ratings_up += 1
    def rate_down(self):
        self.ratings_down += 1
        
        
class Comment(models.Model):
    idx = models.AutoField(primary_key=True)
    board_idx = models.IntegerField(null=False)
    writer = models.CharField(null=False, max_length=50)
    content = models.TextField(null=False)
    post_date = models.DateTimeField(default=datetime.now, blank=True)
    vote = models.IntegerField(null=False)
    ratings_up = models.IntegerField(default=0)
    ratings_down = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    filename = models.CharField(null=True, blank=True, default="", max_length=500)
    filesize = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    image = models.ImageField(default="media/default.jpg", upload_to="media/images")

    def rate_up(self):
        self.ratings_up += 1
    def rate_down(self):
        self.ratings_down += 1

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]

class Profile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    nickname = models.CharField(max_length=64)
    profile_photo = models.ImageField(blank=True)