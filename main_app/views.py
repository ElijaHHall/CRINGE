from django.shortcuts import render
from django.http import HttpResponse
from .models import Message, Contact
from django.contrib.auth.models import AbstractUser

def messages(request):
    messages = Message.objects.all()
    return render(request, 'messages.html', {'messages': messages})

