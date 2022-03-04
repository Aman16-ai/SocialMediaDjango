from email.policy import default
from hashlib import blake2b
from inspect import stack
from turtle import onclick
from unittest import case
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateField, IntegerField
from django.db.models.fields.related import ForeignKey, OneToOneField
from datetime import datetime

# Create your models here.
class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    userauth = OneToOneField(User,on_delete=CASCADE,default=0)
    profile_img = models.ImageField(upload_to="userprofile",blank=True, null=True)
    dob = models.DateField(default=datetime.now)
    country = CharField(max_length=50,blank=True)
    language = CharField(max_length=30,blank=True)
    
    def __str__(self):
        return self.userauth.username
    
    
    @staticmethod
    def getUserProfile(user_id):
        user = UserProfile.objects.get(userauth=user_id)
        return user
    
   
    
class posts(models.Model):
    id = models.AutoField(primary_key=True)
    user_post = models.ForeignKey(UserProfile,on_delete=CASCADE,related_name='userprofile')
    caption = models.CharField(max_length=200)
    post_date = models.DateField(default=datetime.now())
    likes = models.ManyToManyField(UserProfile,related_name="post_likes",null = True,blank=True)
    post_img = models.ImageField(upload_to="userposts")
    likes_count = 0
    def __str__(self):
        return self.caption
      
    @staticmethod
    def getPostById(post_id):
        post = posts.objects.get(id = post_id)
        return post
    @staticmethod  
    def getUserPost(user_id):
        post = posts.objects.get(user_post = user_id)
        return post
    @staticmethod
    def getAllUserPosts(user_id):
        allposts = posts.objects.filter(user_post = user_id)
        return allposts
    @staticmethod
    def getAllPosts():
        return posts.objects.all()        
    
        
    
class Post_comment(models.Model):
    id = models.AutoField(primary_key=True)
    userprofile = models.ForeignKey(UserProfile,on_delete=CASCADE,related_name='userprofile2userprofile')
    post = models.ForeignKey(posts,on_delete=CASCADE)
    reply = models.ForeignKey('self',on_delete= CASCADE,null=True,blank=True)
    comment = models.TextField()
    comment_likes = models.ManyToManyField(UserProfile,null=True,blank=True)
    comment_date = models.DateField(default=datetime.now())
    
    def __str__(self):
       if(len(self.comment) <= 14):
           return "Written by " + self.userprofile.userauth.first_name + self.comment
       else:
           return self.comment[:15]+"..."
    