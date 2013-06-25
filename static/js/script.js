$(".project").click(function(event){
	event.preventDefault()
	var workToShow = works[this.id];
	console.log(works);

	var rsSlider = document.createElement("div");
	rsSlider.style.left = "100%";
	rsSlider.setAttribute("class","royalSlider");
	document.body.appendChild(rsSlider);

	var backButton = document.createElement("a");
	backButton.innerHTML = "Back";
	backButton.style.left = "105%";
	backButton.id = "rsbackButton";
	$(backButton).click(function(){
		rsSlider.style.left = "100%";
		backButton.style.left = "105%";
		setTimeout(function(){
			rsSlider.parentNode.removeChild(rsSlider);
			backButton.parentNode.removeChild(backButton);
		},1000);
	});
	document.body.appendChild(backButton);

	rsSlider.innerHTML = "";
	var newElement = document.createElement("div");
	newElement.setAttribute("class","rsContent");

	var numberofslides = workToShow["Links"].length;
	for(var a = 0; a < numberofslides; ++a){
		var temp = newElement.cloneNode(true)
		temp.innerHTML += "  " + a;
		rsSlider.appendChild(temp);
	}

	var rsSliderChildren = rsSlider.childNodes;

	$(rsSliderChildren[0]).load(workToShow["Links"][0],function(){
		with(rsSlider.style){
			left = "0%";
		}
		backButton.style.left = "5%";

		for(var a = 1; a < rsSliderChildren.length; ++a){
			$(rsSliderChildren[a]).load(workToShow["Links"][a]);
		}

		$(".royalSlider").royalSlider({
			// options go here
			// as an example, enable keyboard arrows nav
			keyboardNavEnabled: true
		});
	});


});

function backGroundChange(){
	for(var a = 0; a < videos.length; ++a){
		if(videos[a]["at"] < scrollFromTop && videos[a]["at"]+(videos[a]["range"]/2) > scrollFromTop && !transitioning){
			if(videos[a]["at"]<scrollFromTop){
				if(a != currentVid){
					transitioning = true;
					if(videos[a]["img"]){
						images.show(videos[a]["img"]-1);
						setTimeout(function(){
							if(useOpacity){
								imageContainer.style.opacity = 1;
							} else {
								imageContainer.style.filter = "alpha(opacity=100)";
							}
							setTimeout(function(){
								transitioning = false;
							});
						},500)
						currentVid = a;
					} else if (videos[a]["mp4"]){
						currentVid = a;
						theVideo.src(videos[currentVid]["mp4"]);
						theVideo.poster(videos[currentVid]["loadImg"])
						theVideo.play();
						setTimeout(function(){
							setTimeout(function(){
								transitioning = false;
							});
							if(useOpacity){
								imageContainer.style.opacity = 0;
							} else {
								imageContainer.style.filter = "alpha(opacity=0)";
							}
						},500);
					}
					highLight(videos[currentVid]["tag"])
				}
			} else if(videos[a]["at"]>scrollFromTop){
				if(a!= 0 && a-1 != currentVid){
					transitioning = true;
					if(videos[a-1]["img"]){
						images.show(videos[a-1]["img"]-1);
						currentVid = a-1;
						setTimeout(function(){
							if(useOpacity){
								imageContainer.style.opacity = 1;
							} else {
								imageContainer.style.filter = "alpha(opacity=100)";
							}
							setTimeout(function(){
								transitioning = false;
							});
						},500)
					} else if (videos[a-1]["mp4"]){
						currentVid = a-1;
						theVideo.src(videos[currentVid]["mp4"]);
						theVideo.play();
						setTimeout(function(){
							setTimeout(function(){
								transitioning = false;
							});
							if(useOpacity){
								imageContainer.style.opacity = 0;
							} else {
								imageContainer.style.filter = "alpha(opacity=0)";
							}
						},500);
					}
					highLight(videos[currentVid]["tag"])
				}
			}
		}
	}
}

function highLight(element){
	var idIn = element;
	var element = document.getElementById(element);
	if(!element){
		element = document.getElementById('aboutLink');
	}
	if(element){
		var siblings = element.parentNode.childNodes;
		$(siblings).each(function(index){
			if(siblings[index].nodeType == 1){
				if(siblings[index] == element && idIn != "remove"){
					element.childNodes[0].setAttribute("class","activeLink");
				} else {
					siblings[index].childNodes[0].setAttribute("class","");
				}
			}
		});

	}
}

$(window).scroll(function(eForEvent){
	scrollFromTop = document.documentElement.scrollTop || document.body.scrollTop;
	for(var a = 0; a < fadingElement.length; ++a){
		fadingElement[a].makeFade(scrollFromTop,windowHeight);
	}
	backGroundChange();
});

$(window).bind("resize",function(){
	windowHeight = windowSize().height;
	for(var a =0 ;a < fadingElement.length; ++a){
		fadingElement[a].resized();
	}
	determinHightsForVids();
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
		$(pages[a]["element"]).click(function(event){
			event.preventDefault();
			goToThisEndPoint("work");
			loadThisEl(this)
		});
		// pages[a]["element"].addEventListener("click", function(event){
		// 	event.preventDefault();
		// 	goToThisEndPoint("work");
		// 	loadThisEl(this)
		// });
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
		$(buttons[buttons.length-1]).click(function(event){
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
		if(useOpacity){
			parentEl.style.opacity = "0";
		} else {
			parentEl.style.filter = "alpha(opacity=0)";
		}
		setTimeout(function(){
			for(var a = 0; a < elements.length; ++a){
				if(buttons[a].id == Element.id){
					with(elements[a].style){
						overflow = "auto";
						display = "block";
					}
				} else {
					//parentEl.style.height = "100%";
					if(useOpacity){
						parentEl.style.opacity = "1";
					} else {
						parentEl.style.filter = "alpha(opacity=100)";
					}
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
	$("#"+link).click(function(event){
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
			var transparency = (scrollLocation-quoteTop)/(height/2); //at half way point we have max opacity
			if(transparency > 0){
				transparency = transparency*-1;
			}
			if(useOpacity){
				quote.style.opacity = 1.2+transparency;
			} else {
				quote.style.filter = "alpha(opacity="+ ((1.2+transparency)*100) + ")";
			}
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
