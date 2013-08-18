from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from datetime import date
import json, random, string

def welcome(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect("/home")
	c = {}
	c.update(csrf(request))
	if request.method == "POST":
		username = request.POST['email']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None and user.profile.is_active:
			login(request, user)
			return HttpResponseRedirect("/home")
		return HttpResponseRedirect("/?message=Invalid Account")
	return render_to_response('welcome.html', c)

def register_user(request):
	if request.method == "POST":
		email    = request.POST['email']
		pwd      = request.POST['password']
		pwd_conf = request.POST['password_conf']
		try:
			u = User.objects.get(username=email)
			return HttpResponse(json.dumps({"response_code": 1, "message": "Email Address Already In Use."}), content_type="application/json")
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
			return HttpResponse(json.dumps({"response_code": 2, "message": "Missmatched Passwords."}), content_type="application/json")

	else:
		return HttpResponse(json.dumps({"response_code": -1}), content_type="application/json")

def confirm_email(request):
	if request.method == "POST":
		email = request.POST['email']
		code  = request.POST['conf_code']
		try:
			u = User.objects.get(username=email)
		except User.DoesNotExist:
			return HttpResponse(json.dumps({"response_code": 3, "message": "User Does Not Exist."}), content_type="application/json")
		p = u.profile
		if p.confirmation_code == code:
			p.is_active = True
			p.save()
			return HttpResponse(json.dumps({"response_code": 0}), content_type="application/json")
		else:
			return HttpResponse(json.dumps({"response_code": 4, "message": "Confirmation Code Does Not Match."}), content_type="application/json")

	else:
		return HttpResponse(json.dumps({"response_code": -1}), content_type="application/json")

def update_user(request):
	if request.method == "POST":
		email = request.POST['email']
		pwd   = request.POST['password']
		fname = request.POST['fname']
		lname = request.POST['lname']
		dname = request.POST['dname']
		dob_month = request.POST['dob_month']
		dob_day = request.POST['dob_day']
		dob_year = request.POST['dob_year']
		try:
			u = User.objects.get(username=email)
		except User.DoesNotExist:
			return HttpResponse(json.dumps({"response_code": 3, "message": "User Does Not Exist."}), content_type="application/json")
		p = u.profile
		p.display_name = dname
		p.date_of_birth = date(month=int(dob_month), day=int(dob_day), year=int(dob_year))
		p.save()
		u.first_name = fname
		u.last_name = lname
		u.save()
		user = authenticate(username=email, password=pwd)
		login(request, user)
		return HttpResponse(json.dumps({"response_code": 0}), content_type="application/json")
	else:
		return HttpResponse(json.dumps({"response_code": -1}), content_type="application/json")

def cancel_registration(request):
	if request.method == "POST":
		email = request.POST['email']
		try:
			u = User.objects.get(username=email)
		except User.DoesNotExist:
			return HttpResponse(json.dumps({"response_code": 0}), content_type="application/json")
		if not u.profile.is_active:
			send_mail('Account Deleted', "Account Deleted", 'donotreply@comiclor.com', [email], fail_silently=False)
			u.delete()
		return HttpResponse(json.dumps({"response_code": 0}), content_type="application/json")

@login_required(redirect_field_name=None)
def coming_soon(request):
	c = {"display_name": request.user.profile.display_name}
	return render_to_response('coming_soon.html', c)

@login_required(redirect_field_name=None)
def logoff(request):
	logout(request)
	return HttpResponseRedirect('/')