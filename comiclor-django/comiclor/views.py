from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

@login_required
def home(request):
	c = {"display_name": request.user.profile.display_name}
	return render_to_response('comiclor/home.html', c)
