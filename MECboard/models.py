from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django import forms
from imagekit.models import ProcessedImageField
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
    image_thumbnail = ProcessedImageField(
            upload_to='media/thumbnail',
            processors=[Thumbnail(100, 100)],
            format='JPEG',
            options={'quality': 60},
            null=True)
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
    evidence = models.BooleanField(default=False, null=False)
    image = models.ImageField(default="media/default.jpg", upload_to="media/images")

    def rate_up(self):
        self.ratings_up += 1
    def rate_down(self):
        self.ratings_down += 1


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]