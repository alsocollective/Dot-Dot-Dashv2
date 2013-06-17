from django.db import models
from django.template.defaultfilters import slugify
import os.path


class ImageNode(models.Model):
	description = models.CharField(max_length=300, blank=True)

	def slugify_filename(instance, filename):
		fname, dot, extension = filename.rpartition('.')
		slug = slugify(fname)
		instance.title = '%s.%s' % (slug, extension)
		return 'static/img/uploaded/%s.%s' % (slug, extension)

	fileType = models.CharField(max_length=100,blank=True)
	location = models.FileField(upload_to=slugify_filename)
	title = models.CharField(max_length=600,blank=True)#,default=titleName)

	def save(self, *args, **kwargs):
		title = os.path.basename(self.location.name)
		self.title = title
		fname, dot, extension = title.rpartition('.')
		self.fileType = extension
		super(ImageNode, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

class TextNode(models.Model):
	title = models.CharField(max_length=600)
	backgroundImage = models.ManyToManyField(ImageNode, blank=True, related_name="bkImage+")
	textField = models.TextField(max_length=4000)

	def __unicode__(self):
		return self.title

class Category(models.Model):
	title = models.CharField(max_length=600)
	slug = models.SlugField(blank=True)
	##if left blank have it display all
	toDisplay = models.IntegerField(blank=True,default=0)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Category, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

class Article(models.Model):
	title = models.CharField(max_length=600)
	textFields = models.ManyToManyField(TextNode,blank=True,related_name="textFields+")
	mediaField = models.ManyToManyField(ImageNode,blank=True,related_name="imageFields+")
	category = models.ManyToManyField(Category,related_name="category+")
	## could add to the save function so it affects the others articles of the same class
	createdDate = models.DateField(auto_now=True)
	slug = models.SlugField(blank=True)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Article, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title
