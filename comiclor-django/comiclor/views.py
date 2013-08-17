from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

@login_required
def home(request):
	c = {"username": request.user.username.split("@")[0]}
	return render_to_response('comiclor/home.html', c)
