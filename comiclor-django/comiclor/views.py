from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

@login_required(redirect_field_name=None)
def home(request):
	c = {"display_name": request.user.profile.display_name}
	return render_to_response('comiclor/home.html', c)

@login_required(redirect_field_name=None)
def library(request):
	c = {"display_name": request.user.profile.display_name}
	return render_to_response('comiclor/library.html', c)

@login_required(redirect_field_name=None)
def cell_creation(request):
	c = {"display_name": request.user.profile.display_name}
	c.update(csrf(request))
	return render_to_response('comiclor/cell_creation.html', c)