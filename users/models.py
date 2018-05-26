from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField

class CustomUser(AbstractUser):
	# First/last name is not a global-friendly pattern
	name = models.CharField(blank=True, max_length=255)
	phone = PhoneField(blank=True, help_text='Contact phone number')
	birth_date = models.DateField(null=True, blank=True)


	def __str__(self):
		return self.email


