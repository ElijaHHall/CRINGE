from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Message, Contact
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

admin.site.register(Message)
admin.site.register(Contact)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'phone', 'birth_date']

admin.site.register(CustomUser, CustomUserAdmin)