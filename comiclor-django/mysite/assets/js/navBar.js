$(function () {
	var navBig = true;
	var toggleNav = function(dir){
		if(dir == "up"){
			$('body').animate({"padding-top":'58px'}, 500);
			$('.navigation .navbar-inner').animate({"height":'58px'}, 500, function(){$('.navigation .navbar-inner').css('overflow','hidden');});
			navBig = false;
		}
		else{
			$('body').animate({"padding-top":'90px'}, 500);
			$('.navigation .navbar-inner').animate({"height":'90px'}, 500, function(){$('.navigation .navbar-inner').css('overflow','');});
			navBig = true;
		}
	};
	$(document).on('scroll', '', function(e){
		if($(this).scrollTop() > 20 && navBig){
			setTimeout(toggleNav("up"), 1000);
		}
		else if($(this).scrollTop() < 20 && !navBig){
			setTimeout(toggleNav("down"), 1000);
		}
	}).on('hover', '.navigation', function(e){
		if(e.type === "mouseenter" && $(document).scrollTop() > 20 && $('.navigation li.dropdown.open').size() === 0){
			setTimeout(toggleNav("down"), 500);
		}
		else if(e.type === "mouseleave" && $(document).scrollTop() > 20 && $('.navigation li.dropdown.open').size() === 0){
			setTimeout(toggleNav("up"), 500);
		}
	});


	$('.dropdown-toggle').dropdown();
});