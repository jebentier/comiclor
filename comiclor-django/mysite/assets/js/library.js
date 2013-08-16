$(function () {
	$(document).on('click', '.library-grouping h3', function(){
		if($(this).find('i').attr('class').indexOf('up') >= 0){
			$(this).find('i').removeClass('icon-chevron-up').addClass('icon-chevron-down');
			$(this).siblings('.library-grouping-content').slideDown();
		}
		else{
			$(this).find('i').addClass('icon-chevron-up').removeClass('icon-chevron-down');
			$(this).siblings('.library-grouping-content').slideUp();
		}
	});
});