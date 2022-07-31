from django.contrib import admin
from django.urls import path , include
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'), 
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('result',views.result),
    path('prepro',views.prepro,name="prepro"),
    path('prog',views.prog,name="prog"),
    path('aug',views.aug,name="aug"),
    path('impre',views.impre,name="impre"),
    path('datasetpre',views.datasetpre,name="datasetpre"),
    path('datasetAfter',views.datasetAfter,name="datasetAfter"),
    path('augb',views.augb,name="augb"),
    path('auga',views.auga,name="auga"),
    path('search',views.search,name="search"),
]
