from django.contrib import admin
from .models import Task

admin.site.register(Task)

"""
# to list all users use:

from django.contrib.auth.models import User
print(list(User.objects.values_list("id", "username", "email")))

# to update user information use:

from django.contrib.auth.models import User
print(list(User.objects.values_list("id", "username", "email")))

#to retrieve a user by ID and update their username and password use:

user = User.objects.get(id=1)
user.username = "new_username"
user.save()

#to set a new password for the user use:

user.set_password("new_password")
user.save()
"""