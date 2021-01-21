from django.urls import path
from . import views

urlpatterns = [
    path('sample/', views.sample, name='sample'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('store/', views.store, name='store'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('', views.home, name='home'),
]
