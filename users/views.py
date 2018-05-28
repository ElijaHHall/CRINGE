from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Message, Contact, CustomUser
from django.contrib.auth.models import AbstractUser
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout


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
