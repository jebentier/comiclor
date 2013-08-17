from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

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

@login_required
def logoff(request):
	logout(request)
	return HttpResponseRedirect('/welcome')

@login_required
def home(request):
	return render_to_response('home.html')