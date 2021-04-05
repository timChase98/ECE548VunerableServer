from django.db import models

# Create your models here.
class Thread(models.Model):
	title = models.CharField(max_length=140)
	authorUserName = models.CharField(max_length=16)

	@property
	def numPosts(self):
		return len(self.post_set.all())

	def __str__(self):
		return self.title

class Post(models.Model):
	userName = models.CharField(max_length=16)
	content = models.CharField(max_length=280)
	thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
	likes = models.IntegerField(default=0)
