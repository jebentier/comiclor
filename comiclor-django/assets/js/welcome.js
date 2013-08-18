$(function () {
	$('#registration').wizard();
	$('.dropdown-date-picker').dropdown_datepicker();

	var updateRegStatus = function(message, id){
		$(id).text(message);
	};

	$(document).on('click', '.form-actions button', function(){
		var csrftoken = $.cookie('csrftoken');
		$.ajaxSetup({
			crossDomain: false,
			beforeSend: function(xhr, settings) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		});
		switch($(this).data('action')){
			case "create":
				$.ajax({
					url: '/register',
					type: 'post',
					data: {
						email: $('.registration-form input[name="email"]').val(),
						password: $('.registration-form input[name="password"]').val(),
						password_conf: $('.registration-form input[name="password_conf"]').val()
					},
					success: function(data){
						if(data['response_code']==0){
							$('li[data-target="#step1"]').removeClass('active');
							$('li[data-target="#step2"]').addClass('active').find('.badge').addClass('badge-info');
							$('#step1').removeClass('active');
							$('#step2').addClass('active');
						}
						else{
							updateRegStatus(data.message, "#email_reg_status");
						}
					},
					error: function(){
						updateRegStatus("Error Contacting Server. Please Try Again Later.", "#email_reg_status");
					}
				});
				break;
			case "confirm":
				$.ajax({
					url: '/confirm_email',
					type: 'post',
					data: {
						email: $('.registration-form input[name="email"]').val(),
						conf_code: $('.registration-form input[name="conf_code"]').val()
					},
					success: function(data){
						if(data['response_code']==0){
							$('li[data-target="#step2"]').removeClass('active');
							$('li[data-target="#step3"]').addClass('active').find('.badge').addClass('badge-info');
							$('#step2').removeClass('active');
							$('#step3').addClass('active');
						}
						else{
							updateRegStatus(data.message, "#email_conf_status");
						}
					},
					error: function(){
						updateRegStatus("Error Contacting Server. Please Try Again Later.", "#email_conf_status");
					}
				});
				break;
			case "update":
				$.ajax({
					url: '/update_user',
					type: 'post',
					data: {
						email: $('.registration-form input[name="email"]').val(),
						password: $('.registration-form input[name="password"]').val(),
						fname: $('.registration-form input[name="fname"]').val(),
						lname: $('.registration-form input[name="lname"]').val(),
						dname: $('.registration-form input[name="dname"]').val(),
						dob_month: $('.dropdown-date-picker').getDatePickerValue("month"),
						dob_day: $('.dropdown-date-picker').getDatePickerValue("day"),
						dob_year: $('.dropdown-date-picker').getDatePickerValue("year")
					},
					success: function(data){
						if(data['response_code']==0){
							window.location = '/home'
						}
						else{
							updateRegStatus(data.message, "#add_info_status");
						}
					},
					error: function(){
						updateRegStatus("Error Contacting Server. Please Try Again Later.", "#add_info_status");
					}
				});
				break;
			case "cancel":
				if($('.registration-content input[name="email"]').val() != ''){
					$.ajax({
					url: '/cancel_registration',
					type: 'post',
					data: {
						email: $('.registration-form input[name="email"]').val(),
					},
					success: function(data){
						if(data['response_code']==0){
							$('.registration-content input').val("");
							$('.current-page').removeClass('current-page');
							$('.registration-form').hide();
							$('.welcome-video').show();
						}
						else{
							alert('error!');
						}
					},
					error: function(){
						updateRegStatus("Error Contacting Server. Please Try Again Later.", "#email_reg_status");
					}
				});
				}
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