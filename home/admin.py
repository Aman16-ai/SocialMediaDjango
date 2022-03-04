from django.contrib import admin
from home.models import UserProfile, posts,Post_comment
# Register your models here.
admin.site.register((UserProfile,posts,Post_comment))