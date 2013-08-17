from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.core.mail import send_mail
import json, random, string

def welcome(request):
	c = {}
	c.update(csrf(request))
	if request.method == "POST":
		username = request.POST['email']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None and user.profile.is_active:
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
			u = User.objects.get(username=email)
			return HttpResponse(json.dumps({"response_code": 1}), content_type="application/json")
		except User.DoesNotExist:
			pass
		if pwd == pwd_conf:
			user = User.objects.create_user(email, email, pwd)
			profile = user.profile
			profile.confirmation_code = ''.join([random.choice(string.digits + string.letters) for i in range(0, 5)])
			profile.save()
			send_mail('Email Confirmation', ''.join(["Here is your confirmation code: ",user.profile.confirmation_code]), 'donotreply@comiclor.com', [email], fail_silently=False)
			user.save()
			return HttpResponse(json.dumps({"response_code": 0, "email": email}), content_type="application/json")
		else:
			return HttpResponse(json.dumps({"response_code": 2, "email": email, "pwd": pwd, "pwd_conf": pwd_conf}), content_type="application/json")

	else:
		return HttpResponse(json.dumps({"response_code": -1}), content_type="application/json")

def confirm_email(request):
	if request.method == "POST":
		email = request.POST['email']
		code  = request.POST['conf_code']
		try:
			u = User.objects.get(username=email)
		except User.DoesNotExist:
			return HttpResponse(json.dumps({"response_code": 3}), content_type="application/json")
		p = u.profile
		if p.confirmation_code == code:
			p.is_active = True
			p.save()
			return HttpResponse(json.dumps({"response_code": 0}), content_type="application/json")
		else:
			return HttpResponse(json.dumps({"response_code": 4}), content_type="application/json")

	else:
		return HttpResponse(json.dumps({"response_code": -1}), content_type="application/json")

def update_user(request):
	if request.method == "POST":
		email = request.POST['email']
		pwd   = request.POST['password']
		fname = request.POST['fname']
		lname = request.POST['lname']
		dname = request.POST['dname']
		try:
			u = User.objects.get(username=email)
		except User.DoesNotExist:
			return HttpResponse(json.dumps({"response_code": 3}), content_type="application/json")
		p = u.profile
		p.display_name = dname
		p.save()
		u.first_name = fname
		u.last_name = lname
		u.save()
		user = authenticate(username=email, password=pwd)
		login(request, user)
		return HttpResponse(json.dumps({"response_code": 0}), content_type="application/json")
	else:
		return HttpResponse(json.dumps({"response_code": -1}), content_type="application/json")

@login_required
def logoff(request):
	logout(request)
	return HttpResponseRedirect('/welcome')