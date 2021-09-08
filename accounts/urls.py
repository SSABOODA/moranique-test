from django.urls import include, path
from rest_framework import urls

from . import views


urlpatterns =[
    path('api-auth/', include('rest_framework.urls')),
    path('signup/', views.UserSignupView.as_view()),
    path('update/<int:pk>', views.UserUpdateView.as_view()),   
 ]
