from django.db import models
from phone_field import PhoneField
from CRINGE import settings

class Message(models.Model):
	body = models.CharField(max_length=250)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	def __str__(self):
		return self.body

class Contact(models.Model):
	name = models.CharField(max_length=100)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

messages = [
    Message('frig off, Rick', 'big_poops'),
    Message('frig off, Mom', 'big_poops'),
    Message('frig off, Janice', 'big_poops'),
    Message('i hate horses', 'big_poops'),
    Message('but also polar horses', 'big_poops'),
]