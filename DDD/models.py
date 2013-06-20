from django.db import models
from django.template.defaultfilters import slugify
import os.path

class MediaNode(models.Model):
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
		super(MediaNode, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

class VideoNode(models.Model):
	title = models.CharField(max_length=300, blank=True)
	videos = models.ManyToManyField(MediaNode, related_name="videos+")
	def __unicode__(self):
		return self.title

class TextNode(models.Model):
	title = models.CharField(max_length=600)
	textField = models.TextField(max_length=4000)
	bkImage = models.ForeignKey(MediaNode,blank=True,null=True,related_name="bkTextImage+")
	bkVideo = models.ForeignKey(VideoNode,blank=True,null=True,related_name="bkTextVideo+")
	slug = models.SlugField(blank=True)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(TextNode, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

class Article(models.Model):
	title = models.CharField(max_length=600)
	textFields = models.ManyToManyField(TextNode,blank=True,related_name="textFields+")
	mediaField = models.ManyToManyField(MediaNode,blank=True,related_name="imageFields+")
	videoURL = models.URLField(max_length=800, blank=True)
	createdDate = models.DateField(auto_now=True)
	slug = models.SlugField(blank=True)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Article, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

class Category(models.Model):
	title = models.CharField(max_length=600)
	slug = models.SlugField(blank=True)
	textFields = models.ManyToManyField(TextNode,blank=True,related_name="rootText+")
	mediaField = models.ManyToManyField(MediaNode,blank=True,related_name="rootMedia+")
	articleFields = models.ManyToManyField(Article,blank=True,related_name="rootArticle+")
	bkImage = models.ForeignKey(MediaNode,blank=True,null=True,related_name="bkImage+")
	bkVideo = models.ForeignKey(VideoNode,blank=True,null=True,related_name="bkVideo+")

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Category, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title
