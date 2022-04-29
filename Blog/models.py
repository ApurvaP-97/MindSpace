from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  #Post model and user model created via admin site will have relationship since user will author the posts
from django.urls import reverse
from taggit.managers import TaggableManager


# Create your models here.
#auto_now=True : Last modifiedUpdate the date post time to curr time. Whenever it was updated
#auto_now_add = True : Created time, but wont let us update it
#timezone.new and not timezone.new() 
#Author is a foreign key 
#on_delete : What if user who created the post gets deleted? Here we will delete the post as well. Not the other way. Deleting user wont delete the post

class Posts(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	 
	date = models.DateTimeField(default=timezone.now) 
	author = models.ForeignKey(User,on_delete = models.CASCADE)  
	tags = TaggableManager()

	def __repr__(self):
		return "Title:{} Created At:{}".format(self.title,self.date)


	#Create view needs a reverse url -> Once created, reverse it back to postDetail - > /post/<pk>
	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})

	#Delete view needs this
	def get_success_url(self):
		return reverse('blog-home') 