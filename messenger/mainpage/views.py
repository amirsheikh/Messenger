from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.contrib.messages import get_messages
from profileapp.models import UserProfile
# Create your views here.
@csrf_protect
def index(request):
    if request.user.is_authenticated:
        User = UserProfile.objects.get_or_create(user = request.user)
        return render(request,"mainpage/index.html", {"name" : User[0].user.first_name,"avatar" : User[0].avatar} )
    return render(request,"mainpage/index.html")