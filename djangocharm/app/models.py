from django.db import models
from django.contrib.auth.models import User
from mongoengine import *
import datetime

# Create your models here.

class UserInfo(models.Model):
	temp = User();
	first_name = models.CharField(max_length = 120,blank = True,null=True)
	last_name = models.CharField(max_length = 120,blank = True,null=True)
	DOB = models.DateField()
	gender = models.CharField(max_length = 120,blank = True,null=True)
	school_name = models.CharField(max_length = 120,blank = True,null=True)
	user = models.OneToOneField(User)
	#password = models.CharField(max_length = 120,blank = True,null=Tr
	parent_email = models.EmailField()
	parent_phone = models.IntegerField()

	def __str__(self):
		return str(self.user.username)

class addtheme(models.Model):
	themename=models.CharField(max_length=100)
	themefile=models.FileField(upload_to='theme')

	def __str__(self):
		return self.themename

class addsubject(models.Model):
	subjectname=models.CharField(max_length=100)
	subjectfile=models.FileField(upload_to='subject')

	def __str__(self):
		return self.subjectname
