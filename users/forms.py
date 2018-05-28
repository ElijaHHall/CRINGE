# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Message, Contact
from dobwidget import DateOfBirthWidget


class CustomUserCreationForm(UserCreationForm):

	class Meta(UserCreationForm.Meta):
		model = CustomUser
		fields = ('username', 'email', 'first_name', 'last_name', 'phone', 'birth_date')
		widgets = {
		'birth_date': DateOfBirthWidget(order='MDY'),
	}

class CustomUserChangeForm(UserChangeForm):

	class Meta:
		model = CustomUser
		fields = UserChangeForm.Meta.fields

class MessageForm(forms.ModelForm):
		
	class Meta:
		model = Message
		fields = ['drinks', 'body']

class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact
		fields = ['name', 'phone']
