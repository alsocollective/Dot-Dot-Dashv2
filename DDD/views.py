from django.shortcuts import render_to_response, get_object_or_404
# from  ALSO.models import Project,Category,Page
#from ALSO.models import ImageNode, TextNode, Category ,Article, InstaPost, Post, Day
def home(request):
	print "yep"
	return render_to_response('index.html',{"nothing":"nothing"})
# import requests
# import json
# from datetime import datetime

# def home(request):
# 	categories = Category.objects.all()
# 	allContent = {}
# 	for category in categories:
# 		catObj = {"cat":category.slug}
# 		articles = Article.objects.all().filter(category__exact = category)
# 		artList = []
# 		for article in articles:
# ## initialze Category
# 			artObj = {"title":article.title,"slug":article.slug,article.slug:"yep"}#, "textFields":article.textFields.all()}
# ## texts
# 			textList = []
# 			for text in article.textFields.all():
# 				textObj = {"text":text.textField,"title":text.title}
# 				for image in text.backgroundImage.all():
# 					textObj.update({"bkImage":image.title})
# 				textList.append(textObj)
# ## images
# 			imageList = []
# 			for image in article.imageFields.all():
# 				imageObj = {"title":image.title}
# 				imageList.append(imageObj)
# ## instegram
# 			instaList = []
# 			allInstaPosts = article.instagramFields.all().order_by('-date')
# 			for i in xrange(0,len(allInstaPosts)-2,2):
# 				subList = ({"message":allInstaPosts[i].message,
# 							"url":allInstaPosts[i].url,
# 							"date":allInstaPosts[i].date.strftime('%Y-%m-%d %H:%M:%S'),
# 							"creator":allInstaPosts[i].creator},{"message":allInstaPosts[i+1].message,
# 							"url":allInstaPosts[i+1].url,
# 							"date":allInstaPosts[i+1].date.strftime('%Y-%m-%d %H:%M:%S'),
# 							"creator":allInstaPosts[i+1].creator})
# 				instaList.append(subList)

# 			# for insta in article.instagramFields.all():
# 			# 	instaObj = {"message":insta.message,"url":insta.url,"date":insta.date.strftime('%Y-%m-%d %H:%M:%S'),"creator":insta.creator}
# 			# 	instaList.append(instaObj)

# ## save
# 			artObj.update({"text":textList,"image":imageList,"insta":instaList})
# 			artList.append(artObj)
# 		catObj.update({"artList":artList})
# 		allContent.update({category.title:catObj})

# 	days=[]
# 	allDays = Day.objects.all()
# 	for dayObj in allDays:
# 		day = {"date":dayObj.date.strftime('%Y-%m-%d')}

# 		postOut = []
# 		for post in dayObj.posts.all():
# 			out = {
# 				post.postType:"type",
# 				"text":post.text,
# 				"poster":post.creator,
# 				"title":post.title,
# 				"slug":post.slug
# 				}
# 			for image in post.image.all():
# 				out.update({"image":image.title})
# 			postOut.append(out)

# 		for image in dayObj.instagramFields.all():
# 			postOut.append({"insta":"type","url":image.url})

# 		day.update({"posts":postOut})
# 		days.append(day)

# 	allContent.update({"days":days})

# 	return render_to_response('index.html',{'allContent':allContent})





# def pureData(request):

# 	return render_to_response('basic.html',{"nothing":"out"})

# def getNewInstaPost(request):
# 	tag = "AlsoCollective"
# 	address = "https://api.instagram.com/v1/tags/%s/media/recent?client_id=f6f99af9459c462d90e826d5893b61f7"%tag
# 	data = json.loads(requests.get(address).content)
# 	allInstaPosts = InstaPost.objects.all()

# 	for image in data["data"]:
# 		isItNew = True
# 		link = image["images"]["standard_resolution"]["url"]

# 		for instance in allInstaPosts:
# 			if instance.url == link:
# 				isItNew = False
# 				print "it's old"
# 				break
# 		if isItNew:
# 			print "new %s" %link
# 			text = image["caption"]["text"]
# 			user = image["caption"]["from"]["username"]
# 			unixtimestamp = int(image["created_time"])
# 			normalTS = datetime.fromtimestamp(unixtimestamp).strftime('%Y-%m-%d %H:%M:%S')
# 			newImage = InstaPost.objects.create(message = text,url = link,date = normalTS,creator = user)
# 			newImage.save()

# 	return render_to_response('basic.html',{"nothing":"out"})



