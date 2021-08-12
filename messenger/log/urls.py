from . import views
from django.urls import path
urlpatterns = [
    path('in/',views.log_in,name = 'log_in'),
    path('out/',views.log_out,name = 'log_out')
]