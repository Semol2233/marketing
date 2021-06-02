from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('',marketing_classview.as_view(),name='homes'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('c/', bkashtotal.as_view(), name='homepage'),



]

