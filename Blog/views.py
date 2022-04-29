from django.shortcuts import render    #django renders templates
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from .models import Posts
from  django.urls import reverse_lazy


# Create your views here.
#This view should be mapped with url. So created urls.py with the same structure as the urls.py in the project. 
#We need to use this home view function in url.py


#Class based view - List View
class PostListView(ListView):
	model = Posts
	#By defualt, class based views look for urls of pattern : <appname>/<mode>_<viewtype>.html -> Blog/Posts_List.html 
	template_name = 'Blog/home.html'
	context_object_name = 'posts'

	#Changing order : Latest Post on Top 
	ordering = ['-date']  # Newest to Oldest


def home(request):
	context = {'posts': Posts.objects.all(), 'title':'Blog Home'} #This key 'posts' can be used in the template to access these posts and the variables(keys in posts dictionaries)
	return render(request,'Blog/home.html',context)   #template name we want to render. Still returns HttpResponse


#Class based view - Detail View
class PostDetailView(DetailView):
	model = Posts

#Class based view - Create View
class PostCreateView(LoginRequiredMixin,CreateView):
	model = Posts
	fields = ['title','content','tags']

	#Validate the form. Always need user id to create new post. Take current logged in user as user creating the post
	def form_valid(self,form):
		form.instance.author = self.request.user
		#Override it here
		return super().form_valid(form)

#Class based view - Update View
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Posts
	fields = ['title','content','tags']

	def form_valid(self,form):
		form.instance.author = self.request.user
		#Override it here
		return super().form_valid(form)


	 #Allow only author to update the corresponding post
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Posts
	success_url = reverse_lazy('blog-home') #Redirect to home page upon delete
	 #Allow only author to delete the corresponding post
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    # Filter posts by tag name  
    posts = Posts.objects.filter(tags=tag)
    context = {
        'tag':tag,
        'posts':posts,
    }
    return render(request, 'Blog/home.html', context)



def about(request):
	return render(request,'Blog/about.html')

def helpline(request):
	return render(request,'Blog/helplines.html')
	