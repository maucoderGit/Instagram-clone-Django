"""Users models."""
# Python
# Django
from django.contrib.auth.models import User
from django.db import models
# Local Apps

class Profile(models.Model):
    """Profile model.
    
    Proxy model that extends the base data with other
    information.

    fields:
    - user: OneToOneField
    """
    # Relations
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # User fields
    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    # Media fields
    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )
    # Date fields
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Returns profile username"""
        return self.user.username


class UserFollowing(models.Model):
    """User following.
    
    This Table use many_to_many relationships and save user's follows and followers.

    fields:
    - user_id = This field save the user id.
    - following_user_id = Field to save followers of a user
    - created = Shows datetime of a user was followed
    """
    # User
    user_id = models.ForeignKey("Profile", related_name="following", on_delete=models.CASCADE)

    # Followed by
    following_user_id = models.ForeignKey("Profile", related_name="followers", on_delete=models.CASCADE)

    # Extra info
    created = models.DateTimeField(auto_now_add=True)
