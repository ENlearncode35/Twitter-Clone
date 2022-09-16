from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table = 'Post'
    name = models.CharField(
        'Name', blank= False, null=False, max_length=14, db_index=True, default='Anonymous'
    )
    body = models.CharField(
        'body', blank=True, null=True, max_length=140, db_index=True
    )
    created_at = models.DateTimeField(
        'Create DateTime', blank=True, auto_now_add=True
    )
    image=CloudinaryField(
        'image',blank=True
    )
    likes=models.PositiveIntegerField(

        'Likes',blank=True,null=True,default=0
    )