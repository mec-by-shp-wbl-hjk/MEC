from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django import forms

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
    
    def hit_up(self):
        self.hit += 1
    def down_up(self):
        self.down += 1
        
        
class Comment(models.Model):
    idx = models.AutoField(primary_key=True)
    board_idx = models.IntegerField(null=False)
    writer = models.CharField(null=False, max_length=50)
    content = models.TextField(null=False)
    post_date = models.DateTimeField(default=datetime.now, blank=True)
    vote = models.IntegerField(null=False)
    

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]