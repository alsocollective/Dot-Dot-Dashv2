from django.contrib import admin
from DDD.models import MediaNode, VideoNode, TextNode, Category, Article, Page

# class ProjectAdmin(admin.ModelAdmin):
# 	fields = ['title','content']

# class CategoryAdmin(admin.ModelAdmin):
# 	fieldsets = [
# 		('title',{'fields':['title']}),
# 		('content',{'fields':['projects','pages']}),
# 	]

class textNodeAdmin(admin.ModelAdmin):
	list_display = ('title', 'textField')
	fieldsets = [
		(None,{'fields':['title','textField']}),
		('backgroundOptions', {
			'classes':('collapse',),
			'fields':('bkVideo','bkImage')
			}),
	]

class pageAdmin(admin.ModelAdmin):
	list_display = ('title', 'pageType')
	fieldsets = [
		(None,{
			'description':('this page represetns a page for each slide, page type determins what the page will display as'),
			'fields':[('title','pageType'),'textFields','mediaField','videoURL','video']
			}),
	]

class categoryAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,{'fields':('title',)}),
		('About,Quote,Contact',{
			'classes':('collapse',),
			'description':("to create new Quotes, add them here, to change About or Contact go to the items that already exist and edit them"),
			'fields':['textFields'],
			}),
		('Work, Services',{
			'classes':('collapse',),
			'description':("Add additional work articles(projects) here, to edit services, find the services that exist and edit it there"),
			'fields':['articleFields'],
			}),
		('Clients',{
			'classes':('collapse',),
			'description':("too add clients Images add them here"),
			'fields':['mediaField'],
			}),
		('backgroundOptions',{
			'classes':('collapse',),
			'fields':('bkVideo','bkImage')
			}),
	]

class articleAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,{'fields':('title',)}),
		('',{
			'classes':('collapse',),
			'description':(""),
			'fields':['textFields'],
			}),
	]

class mediaAdmin(admin.ModelAdmin):
	list_display = ('title','fileType','admin_image')

	fieldsets = [
		(None,{'fields':['location']}),
		('Advance options', {
			'classes':('collapse',),
			'fields':('description','title','fileType')
			}),
	]

class VideoNodeAdmin(admin.ModelAdmin):
	filter_horizontal = ('videos',)




admin.site.register(MediaNode,mediaAdmin)
admin.site.register(VideoNode,VideoNodeAdmin)
admin.site.register(TextNode,textNodeAdmin)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Page,pageAdmin)
