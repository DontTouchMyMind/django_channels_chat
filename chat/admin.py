from django.contrib import admin
from django.contrib.auth.models import User

from .models import Message

admin.site.register(Message)

