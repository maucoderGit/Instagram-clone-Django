"""Posts Models."""
# Python
# Django
from django.db import models
from django.contrib.auth.models import User
# Third packages
# Local modules


class Post(models.Model):
    """Post model."""
    # data
    title = models.CharField(max_length=155)
    photo = models.ImageField(upload_to='posts/photos')
    # datetimes
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # Foreign keys
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    def __str__(self):
        """Return title and username"""
        return f'{self.title} by @{self.user.username}'
