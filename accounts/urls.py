from django.urls import include, path
from rest_framework import urls

from . import views

urlpatterns =[
    path('api-auth/', include('rest_framework.urls')),
    path('signup/', views.UserSignup.as_view()),
    path('list/', views.UserList.as_view()),
    path('delete/<int:pk>', views.UserDelete.as_view()),
 ]
 