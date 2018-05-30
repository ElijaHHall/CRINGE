from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Message, Contact
from django.contrib.auth.models import AbstractUser
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from .credentials import *
from .send_sms import *
from random import randint


class SignUp(generic.CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'

def home(request):
	user_messages = Message.objects.filter(user=request.user)
	user_contacts = Contact.objects.filter(user=request.user)
	return render(request, 'home.html', {'user_messages': user_messages, 'user_contacts': user_contacts})

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/users/login')

# this function will fire message on homepage button click
# you can change the message info in send_sms.py
# so use wisely
def send_message(request):
	user_id = request.GET.get('user_id', None)
	contact_length = len(my_cell)
	message_length = len(my_msg)
	for i in range(contact_length):
		message = client.messages.create(to=my_cell[i], from_=my_twilio, body="You've received a drunk text from" + my_msg[randint(0, message_length-1)])
		print(message_length)
	return HttpResponse(message)


# make an array of messages, and have ajax call a random message on each click


