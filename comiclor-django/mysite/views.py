from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.core.mail import send_mail
import json

def welcome(request):
	c = {}
	c.update(csrf(request))
	if request.method == "POST":
		username = request.POST['email']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None and user.is_active:
			login(request, user)
			return HttpResponseRedirect("/home")
		return HttpResponseRedirect("/welcome?message=Invalid Account")
	return render_to_response('welcome.html', c)

def register_user(request):
	if request.method == "POST":
		email    = request.POST['email']
		pwd      = request.POST['password']
		pwd_conf = request.POST['password_conf']
		try:
			return HttpResponse(json.dumps({"response_code": 1}), content_type="application/json")
		except User.DoesNotExist:
			pass
		if pwd == pwd_conf:
			user = User.objects.create_user(email, email, pwd)
			# send_mail('Email Confirmation', 'Here is your confirmation code: ', 'donotreply@comiclor.com', [email], fail_silently=False)
			user.save()
			return HttpResponse(json.dumps({"response_code": 0, "email": email}), content_type="application/json")
		else:
			return HttpResponse(json.dumps({"response_code": 2}), content_type="application/json")

	else:
		return HttpResponse(json.dumps({"response_code": -1}), content_type="application/json")

@login_required
def logoff(request):
	logout(request)
	return HttpResponseRedirect('/welcome')