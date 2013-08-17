from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	display_name = models.CharField(max_length=50)
	confirmation_code = models.CharField(max_length=10)
	is_active = models.BooleanField(default=False)
	slug = models.SlugField()


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])