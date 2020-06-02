from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', HomeView, name='home'),
    #path('', TeamsView.as_view(), name='home'),
] 