from django.urls import path
from .views import *

urlpatterns=[
    path('',Home.as_view(),name='home'),
    path('about/',About.as_view(),name='about'),
    path('blog/',Blog.as_view(),name='blog'),
    path('class/',Class.as_view(),name='class'),
    path('contact/',Contact.as_view(),name='contact'),
    path('detail/',Detail.as_view(),name='detail'),
    path('team/',Team.as_view(),name='team'),
    path('test/',Test.as_view(),name='test'),
]