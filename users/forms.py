from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()


	#Nested namespace for configs and keeps them in one place. Model that would be affected is User model
	class Meta: #Specify the model that the user wants to interact with
		model = User
		#What are shown and which order
		fields = ['username','email','password1','password2']

		