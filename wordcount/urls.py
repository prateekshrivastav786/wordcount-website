from django.conf.urls import url
from . import views
from django.urls import path
urlpatterns = [
    path('',views.homepage, name='home'),
    path('count/',views.count, name='count'),
    path('about/', views.about, name='aboutme'),
    path('support/', views.supportcenter, name='supportpage'),
    path('supporthandler/', views.supporthandler, name='supporthandler')
]
