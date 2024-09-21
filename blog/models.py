from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()#for large amount of text, since posts can contain many text.
    date_posted=models.DateTimeField(default=timezone.now)#we dont pass timezone.now() as a function, but pass timezone.now as a reference to the function. if we passed it as function i.e using paranthesis, then it would return the time when this model was created, but we pass it as a reference whenever the user creates the post
    author=models.ForeignKey(User,on_delete=models.CASCADE)#author: a ForeignKey linking to the User model. This establishes a many-to-one relationship, meaning each post is written by one user, but each user can write many posts. The on_delete=models.CASCADE parameter specifies that if a user is deleted, all of their posts will also be deleted automatically, which is a common behavior in blog applications to maintain referential integrity.

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk}) #returns the url as a string
