from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
	user = models.OneToOneField(User)
	display_name = models.CharField(max_length=50)
	date_of_birth = models.DateField()
	confirmation_code = models.CharField(max_length=10)
	is_active = models.BooleanField(default=False)
	slug = models.SlugField()

	def confirm_email(code):
		if code == confirmation_code:
			is_active = True
			self.save()
			return True
		else:
			return False