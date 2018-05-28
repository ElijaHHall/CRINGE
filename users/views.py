from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from .models import Message, Contact, CustomUser
from django.contrib.auth.models import AbstractUser
from .forms import CustomUserCreationForm, ContactForm, MessageForm
from django.contrib.auth import authenticate, login, logout


class SignUp(generic.CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'

def home(request):
	user_messages = Message.objects.filter(user=request.user)
	user_contacts = Contact.objects.filter(user=request.user)
	contact_form = ContactForm()
	return render(request, 'home.html', {'user_messages': user_messages, 'user_contacts': user_contacts, 'contact_form': contact_form,})

def post_contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        contact = form.save(commit = False)
        contact.user = request.user
        contact.save()
    return HttpResponseRedirect('/users/home')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/users/login')

