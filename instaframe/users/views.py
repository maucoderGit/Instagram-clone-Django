"""Users views file."""
# Django
from django.contrib.auth import views as auth_views
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Models
from posts.models import Post
from .models import Profile, User
from django.urls import reverse, reverse_lazy

#Forms
from .forms import SignupForm

# Create your views here.

# def login_view(request):
#     """Login view
    
#     This function validate if a user exists and logs in
#     if credentials are validated sucesfully.

#     Parameters:
#     - request: Dict
#         - username: str
#         - password: str

#     returns a user logged and reddirect to feed page.
#     """
#     if request.user.is_authenticated:
#         return redirect("posts:feed")
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             return redirect('posts:feed')
#         else:
#             return render(request, 'users/login.html', {'error': 'Invalid username or/and password!'})
#     return render(request, 'users/login.html')


# @login_required
# def logout_view(request):
#     """Logout view.
    
#     This function use the django authentication system
#     and logout a user.

#     - parameters:
#         - request: HTTPRequest

#     redirects a users to login view and logout them
#     """
#     logout(request)
#     return redirect('users:login')


# def signup_view(request):
#     """Signup view.
    
#     This function usus django authenticate and forms
#     to validate and create a user instance in database
    
#     parameters:
#     - request: HTTPRequest

#     returns a user instance to database models
#     """
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('users:login')
#     else:
#         form = SignupForm()
    
#     return render(
#         request=request,
#         template_name='users/signup.html',
#         context={
#             'form': form
#         }
#     )
        

# @login_required
# def update_profile(request):
#     """Update a user's profile view
    
#     user's profile owner can modify their profile using this views.

#     parameters:
#     - request: HTTPProtocol
#     """
#     profile = request.user.profile
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             data = form.cleaned_data

#             # save data
#             profile.website = data['website']
#             profile.phone_number = data['phone_number']
#             profile.biography = data['biography']
#             profile.picture = data['picture']
#             profile.save()

#             # message
#             messages.success(request, 'Your profile has been updated!')

#             url = reverse(('users:update_profile'), kwargs={'username': request.user.username})

#             return redirect(url)
#     else:
#         form = ProfileForm()

#     return render(
#         request=request,
#         template_name='users/update_profile.html',
#         context={
#             'profile': profile,
#             'user': request.user,
#             'form': form
#         }
#     )

# Class Bases views

class LoginView(auth_views.LoginView):
    """Login view
    
    This function validate if a user exists and logs in
    if credentials are validated sucesfully.
    """
    redirect_authenticated_user: bool = True
    template_name: str = 'users/login.html'


class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view.
    
    This function use the django authentication system
    and logout a user if the user is logged.

    redirects a users to login view when the user did logout.
    """
    template_name: str = 'users/logged_out.html'


class SignupView(FormView):
    """Signup view.
    
    This function usus django authenticate and forms
    to validate and create a user instance in database
    
    parameters:
    - request: HTTPRequest

    returns a user instance to database models
    """
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data"""
        form.save()
        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update a user's profile view
    
    user's profile owner can modify their profile using this views.

    parameters:
    - request: HTTPProtocol
    """

    template_name: str = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self) -> Profile:
        """Returns user's profile."""
        return self.request.user.profile
    
    def get_success_url(self) -> str:
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})


class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view.
    
    Show a user profile page, using django templates
    
    parameters:
    - request: HTTPRequest

    returns a profile detail page with all the post of the user getted with the slug.
    """
    model = User
    slug_field: str = 'username'
    slug_url_kwarg: str = 'username'
    template_name = 'users/detail.html'
    context_object_name: str = 'user'

    def get_context_data(self, **kwargs):
        """add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user: User = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')

        return context