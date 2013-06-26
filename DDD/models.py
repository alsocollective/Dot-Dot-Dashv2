from django.db import models
from django.template.defaultfilters import slugify
import os.path

class MediaNode(models.Model):
	description = models.CharField(max_length=300, blank=True)

	def slugify_filename(instance, filename):
		fname, dot, extension = filename.rpartition('.')
		slug = slugify(fname)
		instance.title = '%s.%s' % (slug, extension)
		return 'static/uploaded/%s.%s' % (slug, extension)
	fileType = models.CharField(max_length=100,blank=True)
	location = models.FileField(upload_to=slugify_filename)
	title = models.CharField(max_length=600,blank=True)#,default=titleName)
	slug = models.CharField(max_length=500,blank=True)

	def save(self, *args, **kwargs):
		title = os.path.basename(self.location.name)
		self.title = title
		fname, dot, extension = title.rpartition('.')
		self.slug = slugify(title)
		self.fileType = extension
		super(MediaNode, self).save(*args, **kwargs)


	def admin_image(self):
		if(self.fileType == "jpg" or self.fileType == "png" or self.fileType == "tiff" or self.fileType == "gif"):
			return '<img style="width:200px;height:auto;" src="/static/uploaded/%s"/>' % self.title
		return "not an Image"
	admin_image.allow_tags = True

	def __unicode__(self):
		return self.title

	url = models.URLField(max_length=800, blank=True)


class VideoNode(models.Model):
	title = models.CharField(max_length=300, blank=True)
	videos = models.ManyToManyField(MediaNode, related_name="videos+")
	image = models.ForeignKey(MediaNode,blank=True,null=True,related_name="imageFallBack+")

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

class Page(models.Model):
	pageTypes = (
		("text","text"),
		("singleImage","singleImage"),
		("fourImage","fourImage"),
		("sixImage","sixImage"),
		("imageWText","imageWText")
	)
	title = models.CharField(max_length=600)
	textFields = models.ManyToManyField(TextNode,blank=True,related_name="texts+")
	mediaField = models.ManyToManyField(MediaNode,blank=True,related_name="images+")
	videoURL = models.URLField(max_length=800, blank=True)
	pageType = models.CharField(max_length=30, choices=pageTypes)
	video = models.ForeignKey(VideoNode,blank=True,null=True,related_name="videoPage+")
	slug = models.SlugField(blank=True)

	def save(self,*args, **kwargs):
		self.slug = slugify(self.title)
		super(Page, self).save(*args, **kwargs)


	def __unicode__(self):
		return self.title

class Article(models.Model):
	title = models.CharField(max_length=600)
	pages = models.ManyToManyField(Page,blank=True,related_name="pages+")
	textFields = models.ManyToManyField(TextNode,blank=True,related_name="textFields+")
	mediaField = models.ManyToManyField(MediaNode,blank=True,related_name="imageFields+")
	videoURL = models.URLField(max_length=800, blank=True)
	createdDate = models.DateField(auto_now=True)
	slug = models.SlugField(blank=True)
	description = models.ForeignKey(TextNode,related_name="textDescription+")

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
