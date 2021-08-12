from . import views
from django.urls import path
urlpatterns = [
    path('editprofile/',views.editprofile,name = 'editprofile')
]