$(function () {
	$('#registration').wizard();
	$(document).on('click', '.form-actions button', function(){
		switch($(this).data('action')){
			case "create":
				$('li[data-target="#step1"]').removeClass('active');
				$('li[data-target="#step2"]').addClass('active').find('.badge').addClass('badge-info');
				$('#step1').removeClass('active');
				$('#step2').addClass('active');
				break;
			case "confirm":
				$('li[data-target="#step2"]').removeClass('active');
				$('li[data-target="#step3"]').addClass('active').find('.badge').addClass('badge-info');
				$('#step2').removeClass('active');
				$('#step3').addClass('active');
				break;
			case "update":
				
				break;
			case "cancel":
				$('.registration-content input').val("");
				$('.current-page').removeClass('current-page');
				$('.registration-form').hide();
				$('.welcome-video').show();
				break;
			default:
				console.log("action not permitted!");
		}
	}).on('click', 'li#open-registration', function(){
		$('.current-page').removeClass('current-page');
		$(this).addClass('current-page');
		$('.registration-form').show();
		$('.welcome-video').hide();
		$('.login-form').hide();
	}).on('click', 'li#open-signin', function(){
		$('.current-page').removeClass('current-page');
		$(this).addClass('current-page');
		$('.login-form').show();
		$('.registration-form').hide();
		$('.welcome-video').hide();
	}).on('click', 'li a', function(e){
		e.preventDefault();
	});
});