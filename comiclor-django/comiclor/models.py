from django.db import models
from django.contrib.auth.models import User
from datetime import date

"""
	User Profile
	Connected to a user account to allow for additional information storage
	- Display Name
	- Email Confirmation Code
	- Custom Active Boolean
	- Account Slug 
	- Date Of Birth
"""

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	display_name = models.CharField(max_length=50)
	confirmation_code = models.CharField(max_length=10)
	is_active = models.BooleanField(default=False)
	slug = models.SlugField()
	date_of_birth = models.DateField(default=date.today)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])