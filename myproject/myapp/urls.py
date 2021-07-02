from django.urls import path
from .views import home,about,cont,software,ai,cloud
urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('cont/',cont,name='cont'),
    path('software/',software,name='softrware'),
    path('ai/',ai,name='ai'),
    path('cloud/',cloud,name='cloud'),
]