"""Posts views."""

# Django
from typing import Any, Optional
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

# Forms
from posts.forms import PostForm

# Models
from .models import Post

# Utilities


# Create your views here.
@login_required
def lists_posts_views(request):
	"""A basic view"""
	posts: list = Post.objects.all().order_by('-created')

	return render(request, 'posts/feed.html', {'posts': posts})


class CreatePostView(LoginRequiredMixin, CreateView):
	"""Create a new Post.
	
	This view creates posts if the user is logged.
	"""
	
	template_name: str = 'posts/new.html'
	form_class = PostForm
	success_url: Optional[str] = reverse_lazy('posts:feed')

	def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
		context = super().get_context_data(**kwargs)
		context['user'] = self.request.user
		context['profile'] = self.request.user.profile
		return context


# Brokes DRY principies
# @login_required
# def create_post(request):
# 	"""Create Post.
	
# 	This view creates a new post
	
# 	parameters:
# 	- request: HTTPMethods

# 	Redirects to the feed url in post app.
# 	"""
# 	if request.method == 'POST':
# 		form = PostForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('posts:feed')
# 	else:
# 		form = PostForm()
	
# 	return render(
# 		request=request,
# 		template_name='posts/new.html',
# 		context={
# 			'form': form,
# 			'user': request.user,
# 			'profile': request.user.profile
# 		}
# 	)

# Class based Views

class PostsFeedView(LoginRequiredMixin, ListView):
	"""Post Feed View.
	
	Display all the published posts in feed.

	Requirements:
	- User must to be logged
	"""

	template_name = 'posts/feed.html'
	model = Post
	ordering = ('-created', )
	paginate_by = 40
	context_object_name: str = 'posts'


class PostDetailView(LoginRequiredMixin, DetailView):
	"""Post Detail View.
	
	Display posts by pk.
	"""
	model = Post
	slug_field: str = 'pk'
	slug_url_kwarg: str = 'pk'
	template_name = 'posts/detail.html'
	context_object_name: str = 'post'