from django.db import models

# Create your models here.

class Article(models.Model):
	''' a single article '''
	title = models.TextField(blank=True)
	abstract = models.TextField(blank=True)
	authors = models.TextField(blank=True)
	doi = models.CharField(max_length=255)

	def __unicode__(self):
		self.title

class Feed(models.Model):
	url = models.URLField(max_length=255)
	