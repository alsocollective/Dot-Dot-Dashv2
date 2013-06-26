from django.shortcuts import render_to_response, get_object_or_404
from DDD.models import Category

def home(request):
	return render_to_response('index.html',{"nothing":"nothing"})

def basic(request):
	if(request.mobile):
		print "MOBILE VERSION!!!!"
		quotes = Category.objects.all().filter(title = "Quote")[0]
		print quotes
		return render_to_response("mobile/index.html",getText(quotes.textFields.all()))
	else:
		print "normal version"
	categories = Category.objects.all()
	out = {};
	for cat in categories:
		catObj = {"title":cat.title,"slug":cat.slug}
		catObj.update(getImages(cat.mediaField.all()))
		catObj.update(getText(cat.textFields.all()))
		catObj.update(getArticle(cat.articleFields.all()))

		if cat.bkVideo:
			catObj.update(getBkVid(cat.bkVideo))
		if cat.bkImage:
			catObj.update(getBkImg(cat.bkImage))
#		catObj.update(checkBk(cat))

		#catObj.update(projectList(cat.pages.all()))

		out.update({cat.title:catObj})
	return render_to_response("index.html",{"categories":out})


def about(request):
	data = Category.objects.all().filter(title = "About")[0]
	return render_to_response("mobile/about.html",getText(data.textFields.all()))

def services(request):
	data = Category.objects.all().filter(title = "Services")[0].articleFields.all()[0]
	#print data
	out = getText(data.textFields.all())
	out["text"].insert(0,{"location":data.title,"type":data.description.textField})
	return render_to_response("mobile/services.html",out)

def clients(request):
	data = Category.objects.all().filter(title = "Clients")[0]
	return render_to_response("mobile/clients.html",getImages(data.mediaField.all()))

def work(request):
	data = Category.objects.all().filter(title = "Work")[0].articleFields.all()
	return render_to_response("mobile/work.html",getArticle(data))
	#return render_to_response("mobile/view")

def works(request,project=None):
	work = Category.objects.filter(slug = "work")[0]
	article = work.articleFields.filter(slug = project)
	data = article[0].pages.all()
	out = {"title":article[0].title};
	pages = []
	for page in data:
		pageObj = {"page":page.title}
		pageObj.update(getText(page.textFields.all()))
		pageObj.update(getImages(page.mediaField.all()))
		pages.append(pageObj)
	out.update({"pages":pages})
	return render_to_response("mobile/works.html",{"page":out})











def getBkImg(imageIn):
	return {"bkImg":{imageIn.fileType:"type","type":imageIn.fileType,"location":imageIn.title}}

def getBkVid(videoIn):
	videos = []
	for video in videoIn.videos.all():
		videos.append({video.fileType:"type","type":video.fileType,"location":video.title})
	return {"bkVid":videos,"placeHold":videoIn.image}

def projects(request,project=None,page=None):
	if(project == None or page == None):
		return render_to_response("basic.html",{"none":"data"})

	work = Category.objects.filter(slug = "work")[0]

	article = work.articleFields.filter(slug = project)
	if(len(article) <= 0):
		return render_to_response("basic.html",{"none":"data"})

	pages = article[0].pages.filter(slug = page)
	if(len(pages) <= 0):
		return render_to_response("basic.html",{"none":"data"})
	pages = pages[0]

	pageObj = {"title":pages.title}
	pageType = pages.pageType;

	if(pageType == "imageWText"):
		pageObj.update(getText(pages.textFields.all()))
		if pages.videoURL:
			pageObj.update({"vidLink":pages.videoURL})
		pageObj.update(getImages(pages.mediaField.all()))
	if(pageType == "fourImage" or pageType == "singleImage"):
		pageObj.update(getImages(pages.mediaField.all()))


	return render_to_response("%s.html"%pageType,{"project":article,"content":pageObj})


# def projectList(listOfProjects):
# 	print listOfProjects
# 	return {"":""}



#with a list of Articles, itterate and return an array of pages
def getArticle(listIn):
	if(listIn):
		articles = []
		for article in listIn:
			artObj = {"subHead":article.description.title, "description":article.description.textField, "title":article.title,"slug":article.slug,"text":getText(article.textFields.all())}
			artObj.update(getPages(article.pages.all()))
			articles.append(artObj)
		return {"articles":articles}
	return {"":""}

#with an article, return all of it;s pages With relevant content
def getPages(listIn):
	if(listIn):
		pages = []
		for page in listIn:
			pageObj = {"slug":page.slug,"type":page.pageType}
			pages.append(pageObj)
		return {"pages":pages}
	return {"":""}

##check if there is bk, return it if there is
def checkBk(obj):
	if obj.bkImage:
		return ({"bkImg":obj.bkImage})
	if obj.bkVideo:
		videos = []
		for vid in obj.bkVideo.videos.all():
			videos.append({"type":vid.fileType,"name":vid.title})
		return ({"bkVid":videos,"placeHold":obj.bkVideo.image})
	return {"":""}

##take a list of texts and return a json of them
def getText(listIn):
	textList = []
	for text in listIn:
		textObj = {"type":text.textField,"location":text.title,"slug":text.slug}
		textObj.update(checkBk(text))

		textList.append(textObj)
	return ({"text":textList})

##take a list of images and return a json of them
def getImages(listIn):
	mediaList = []
	for media in listIn:
		mediaObj = {media.fileType:"type","type":media.fileType,"location":media.title,"slug":media.slug}
		mediaList.append(mediaObj)
	return ({"media":mediaList})

