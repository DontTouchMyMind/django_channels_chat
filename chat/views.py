import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.safestring import mark_safe


def index(request):
    user_list = User.objects.all()

    context = {
        'title': 'ListUser',
        "users_list": user_list
    }
    return render(request, 'chat/index.html', context)


@login_required
def room(request, room_name):
    user_list = User.objects.all()
    context = {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
        "users_list": user_list

    }

    return render(request, 'chat/room.html', context)

