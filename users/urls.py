from django.urls import path
from . import views

urlpatterns = [
	path('signup/', views.SignUp.as_view(), name='signup'),
	path('home/', views.home, name='home'),
	path('logout/', views.logout_view, name='logout'),
	path('home/post_contact/', views.post_contact, name='post_contact')
]
