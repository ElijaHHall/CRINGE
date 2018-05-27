from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from .models import Message, Contact
from django.contrib.auth.models import AbstractUser
from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'

def messages(request):
	messages = Message.objects.all()
	return render(request, 'messages.html', {'messages': messages})