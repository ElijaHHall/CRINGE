from django.urls import path
from . import views

urlpatterns = [
	path('home/', views.home, name='home'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('send_message/', views.send_message, name='send_message')
]
