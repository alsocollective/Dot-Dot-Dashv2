var scrollFromTop = 0;
var windowHeight = windowSize().height;


var fadingElement = [
	new FadeingObject("openingQuote"),
	new FadeingObject("optimismQuote"),
	new FadeingObject("collaboQuote")
];
//set up the elements if the are in view

for(var a = 0; a < fadingElement.length; ++a){
	fadingElement[a].makeFade(scrollFromTop,windowHeight);
}

addEvent("aboutLink","about");
addEvent("serviceLink","services");
addEvent("clientsLink","clients");
addEvent("ourWorkLink","work");
addEvent("contactLink","contact");

//goes what to be displayed, then button, display button
var ServiceButtons = new Buttons(["basicService","serviceLink","branding","brandingButton","socMed","socMedButton","research","researchButton"]);

var slideOptions = {
	"mainContainer":"mainContainer",
	"leftContainer": "leftContainer",
	"rightContainer":"rightContainer",
	"loadTo":"rightContainer",
	"pagesToLoad":[
		{"id":"patch","link":"work/patch.html"},
		{"id":"antica","link":"work/antica.html"},
		{"id":"singhampton","link":"work/singhampton.html"},
		{"id":"patagonia","link":"work/patagonia.html"}
	]
};

var Works = new Slide(slideOptions);

document.getElementById("ourWorkLink").addEventListener('click', function(event){
	Works.backToMenue();
});

//Nav
$("#largeLogo").one('load',function(){						//when the image loads do this
	$(setUpStaticLocationOfSticky(false)).waypoint(function(){ 	//setUpStaticLocationOfSticky returns an emement
		$("#sticky_navigation").toggleClass("nav_fixed");
		$(".squareLogoHide").toggleClass("squareLogo");
	})
}).each(function() {
	if(this.complete) $(this).load();
}).error(function(){
	$(setUpStaticLocationOfSticky(72)).waypoint(function(){ 	//we give an argument of a potential hight
		$("#sticky_navigation").toggleClass("nav_fixed");
		$(".squareLogoHide").toggleClass("squareLogo");
	})
});



var videos = [
	{"range":400,"parent":document.getElementById("openingQuote"),"tag":"remove","mp4":[
		{type: "video/mp4", src: "http://localhost/videos/Lightning/Lightning.mp4"},
		{type: "video/webm", src: "http://localhost/videos/Lightning/Lightning.webm"},
		{type: "video/ogv", src: "http://localhost/videos/Lightning/Lightning.ogv"}
	]},
	{"range":400,"parent":document.getElementById("about"),"tag":"aboutLink","img":1},
	{"range":400,"parent":document.getElementById("services"),"tag":"serviceLink","img":2},
	{"range":400,"parent":document.getElementById("clients"),"tag":"clientsLink","img":3},
	{"range":400,"parent":document.getElementById("work"),"tag":"ourWorkLink","mp4":[
		{type: "video/mp4", src: "http://localhost/videos/River/River.mp4"},
		{type: "video/webm", src: "http://localhost/videos/River/River.webm"},
		{type: "video/ogv", src: "http://localhost/videos/River/River.ovg"}
	]},
	{"range":400,"parent":document.getElementById("collaboQuote"),"img":4},
	{"range":400,"parent":document.getElementById("contact"),"tag":"contactLink","mp4":[
		{type: "video/mp4", src: "http://localhost/videos/Waterfall/Waterfall1.mp4"},
		{type: "video/webm", src: "http://localhost/videos/Waterfall/Waterfall1.webm"},
		{type: "video/ogv", src: "http://localhost/videos/Waterfall/Waterfall1.ogv"}
	]}
];

//find the location at which these elements occure
determinHightsForVids();


var currentVid = 0;

var videoContainer = document.getElementById("vid_1");
var imageContainer = document.getElementById("bkStrechImage");

var images = $(imageContainer).backstretch([
	'img/BK1.jpg',
	'img/BK2.jpg',
	'img/BK3.jpg',
	'img/BK4.jpg'
], {fade: 500}).data('backstretch').pause();
imageContainer.style.opacity = 0;

var theVideo = _V_("vid_1",{"loop": "true","autoplay": true,"controls": false});
theVideo.ready(function(){
	theVideo.src(videos[0]["mp4"]);
	theVideo.play();
	theVideo.volume(0);
});

var transitioning = false;

function backGroundChange(){
	for(var a = 0; a < videos.length; ++a){
		if(videos[a]["at"]-(videos[a]["range"]/2) < scrollFromTop && videos[a]["at"]+(videos[a]["range"]/2) > scrollFromTop && !transitioning){
			if(videos[a]["at"]<scrollFromTop){
				if(a != currentVid){
					transitioning = true;
					if(videos[a]["img"]){
						imageContainer.style.opacity = 1;
						images.show(videos[a]["img"]-1);
						setTimeout(function(){
							transitioning = false;
						},500)
						currentVid = a;
					} else if (videos[a]["mp4"]){
						currentVid = a;
						theVideo.src(videos[currentVid]["mp4"]);
						theVideo.play();
						setTimeout(function(){
							transitioning = false;
							imageContainer.style.opacity = 0;
						},500);
					}
					highLight(document.getElementById(videos[currentVid]["tag"]))
				}
			} else if(videos[a]["at"]>scrollFromTop){
				if(a!= 0 && a-1 != currentVid){
					transitioning = true;
					if(videos[a-1]["img"]){
						imageContainer.style.opacity = 1;
						images.show(videos[a-1]["img"]-1);
						currentVid = a-1;
						setTimeout(function(){
							transitioning = false;
						},500)
					} else if (videos[a-1]["mp4"]){
						currentVid = a-1;
						theVideo.src(videos[currentVid]["mp4"]);
						theVideo.play();
						setTimeout(function(){
							transitioning = false;
							imageContainer.style.opacity = 0;
						},500);
					}
					highLight(document.getElementById(videos[currentVid]["tag"]))
				}
			}
		}
	}
}

function highLight(element){
	if(element){
		var siblings = element.parentNode.childNodes;
		$(siblings).each(function(index){
			if(siblings[index].nodeType == 1){
				if(siblings[index] == element){
					element.childNodes[0].setAttribute("class","activeLink");
				} else {
					siblings[index].childNodes[0].setAttribute("class","");
				}
			}
		});

	}
}

window.addEventListener("scroll",function(eForEvent){
	scrollFromTop = document.documentElement.scrollTop || document.body.scrollTop;
	for(var a = 0; a < fadingElement.length; ++a){
		fadingElement[a].makeFade(scrollFromTop,windowHeight);
	}
	backGroundChange();
});

window.addEventListener("resize",function(){
	windowHeight = windowSize().height;
	for(var a =0 ;a < fadingElement.length; ++a){
		fadingElement[a].resized();
	}
	determinHightsForVids();
	//ServiceButtons.position();
});

/////////////////
//OUR FUNCTIONS//
/////////////////

function determinHightsForVids(){
	for(var a = 0; a < videos.length; ++a){
		videos[a]["at"] = getPageTopLeft(videos[a]["parent"]).top;
	}
}

function Slide(options){

	var mainC = document.getElementById(options["mainContainer"]);
	var lC = document.getElementById(options["leftContainer"]);
	var rC = document.getElementById(options["rightContainer"]);
	var loadingArea = document.getElementById(options["loadTo"]);
	var pages = options["pagesToLoad"];
	var buttons = [];

	for(var a = 0; a < pages.length; ++a){
		pages[a]["element"] = document.getElementById(pages[a]["id"]);
		pages[a]["element"].addEventListener("click", function(event){
			event.preventDefault();
			goToThisEndPoint("work");
			loadThisEl(this)
		});
	}

	function hideMenue(){
		with(mainC.style){
			left = "-100%";
		}
	}

	function loadThisEl(element){
		for(var a =0; a < pages.length; ++a){
			if(element.id == pages[a]["id"]){
				//possibly add the function to the canavs the size of window-menue bar
				$(loadingArea).load(pages[a]["link"]);
				$(loadingArea).ready(function(){
					hideMenue();
				})
			}
		}
	}

	function showMenue(){
		with(mainC.style){
			left = "0%";
		};
	}

	this.backToMenue = function(){
		showMenue();
	}
}

//pass object to show, then button to hide
function Buttons(tags){
	var elements = [];
	var buttons = [];

	for(var a = 0; a < tags.length; ++a){
		elements.push(document.getElementById(tags[a]));
		++a;
		buttons.push(document.getElementById(tags[a]))
		buttons[buttons.length-1].addEventListener("click", function(event){
			event.preventDefault();
			hideAllBut(this);
		});
	}

	var parentEl = elements[0].parentNode;

	elements[0].style.display = "block";


	var parent = buttons[1].parentNode.parentNode;
	var absoluteParent = parent.parentNode;

	function hideAllBut(Element){
		//parentEl.style.height = "0%";
		parentEl.style.opacity = "0";
		setTimeout(function(){
			for(var a = 0; a < elements.length; ++a){
				if(buttons[a].id == Element.id){
					with(elements[a].style){
						overflow = "auto";
						display = "block";
					}
				} else {
					//parentEl.style.height = "100%";
					parentEl.style.opacity = "1";
					with(elements[a].style){
						overflow = "hidden";
						display = "none";
					}
				}
			}
		},500);
	}

	this.position = function(){
		var topOut = (absoluteParent.clientHeight - parent.clientHeight);
		with(parent.style){
			position = "absolute";
			top = topOut;
		}
	}

}

function addEvent(link, endPoint){
	document.getElementById(link).addEventListener('click', function(event){
		event.preventDefault();
		goToThisEndPoint(endPoint);
	});
}

function goToThisEndPoint(location){
	var top = getPageTopLeft(document.getElementById(location)).top;
	var body = $("body,html");
	if(location == "work"){
		top;
	}
	$(body).animate({scrollTop : top+100},1000);
	setTimeout(function(){
		backGroundChange()
	},1600);
	setTimeout(function(){
		//wait till after the scroll
		setHashTag(location);
	},1100);
}

function setHashTag(newTag){
	var element = document.getElementById(newTag);
	element.id = "";
	window.location.replace("#"+newTag);
	element.id = newTag;
}

function setUpStaticLocationOfSticky(didNotLoad){		//loaded can either come in as false, or a value
	var newElement = document.createElement("div");
	newElement.id= "staticSticky";

	var logoHight = getPageTopLeft(document.getElementById("aboutLink")).top;

	newElement.style.marginTop =  (logoHight) +"px";
	document.body.insertBefore(newElement,document.body.firstChild)
	return newElement;
}

function FadeingObject(element){
	var quote = document.getElementById(element);
	var quoteTop = getPageTopLeft(quote).top;
	var quoteSize = $(quote).height();

	this.resized = function(){
		quoteTop = getPageTopLeft(quote).top;
		quoteSize = $(quote).height();
	}

	this.makeFade = function(scrollLocation,height){
		if(scrollLocation > quoteTop - height + quoteSize/2 && scrollLocation < quoteTop + height + quoteSize/2){
			//var transparency = (scrollLocation-quoteTop+(height/2))/height/4*10;
			var transparency = (scrollLocation-quoteTop)/(height/2); //at half way point we have max opacity
			if(transparency > 0){
				transparency = transparency*-1;
			}
			quote.style.opacity = 1.2+transparency;
		}
	}
}

function getPageTopLeft(el) {
	var rect = el.getBoundingClientRect();
	var docEl = document.documentElement;
	return {
		left: rect.left + (window.pageXOffset || docEl.scrollLeft || 0),
		top: rect.top + (window.pageYOffset || docEl.scrollTop || 0)
	};
}

function windowSize() {
  var myWidth = 0, myHeight = 0;
  if( typeof( window.innerWidth ) == 'number' ) {
    //Non-IE
    myWidth = window.innerWidth;
    myHeight = window.innerHeight;
  } else if( document.documentElement && ( document.documentElement.clientWidth || document.documentElement.clientHeight ) ) {
    //IE 6+ in 'standards compliant mode'
    myWidth = document.documentElement.clientWidth;
    myHeight = document.documentElement.clientHeight;
  } else if( document.body && ( document.body.clientWidth || document.body.clientHeight ) ) {
    //IE 4 compatible
    myWidth = document.body.clientWidth;
    myHeight = document.body.clientHeight;
  }

  return {
  	"width": myWidth,
  	"height": myHeight
  }
}
