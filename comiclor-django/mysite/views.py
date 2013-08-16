from django.views.generic import TemplateView
from django.shortcuts import render

class WelcomeView(TemplateView):
	template_name = "welcome.html"