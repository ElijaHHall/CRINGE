from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField
from CRINGE import settings

class CustomUser(AbstractUser):
	name = models.CharField(blank=True, max_length=255)
	phone = PhoneField(blank=True, help_text='Contact phone number')
	birth_date = models.DateField(null=True, blank=True)


	def __str__(self):
		return self.email

class Message(models.Model):
	body = models.CharField(max_length=250)
	drink = models.IntegerField(default=0)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	def __str__(self):
		return self.body

class Contact(models.Model):
	name = models.CharField(max_length=100)
	phone = PhoneField(blank=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
