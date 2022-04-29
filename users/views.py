from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm


#messages.debug, success, warning, error

# Create your views here.
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		#Validating the form data
		if form.is_valid():

			#create a user when form is valid. Only then can you view from admin side
			form.save()
			username = form.cleaned_data.get('username')
			
			#Flash message. Should be updated in the template. We can put this in base template(The nav bar is common across all pages)
			messages.success(request, f'Hi {username}, Welcome to MindSpace!')

			#Now redirect this to home page #url pattern for home page
			return redirect('login')

	else:
		form = UserRegisterForm()


	return render(request,'users/register.html',{'form':form})


def profile(request):
	return render(request, 'users/profile.html')