from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete = models.DO_NOTHING)
	description = models.CharField(max_length=200, default='')
	department = models.CharField(max_length=100, default='')

class Course(models.Model):
	course = models.CharField(max_length=100)
	students = models.ManyToManyField(UserProfile)

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user = kwargs['instance'])
		
post_save.connect(create_profile, sender=User)
