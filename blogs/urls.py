from django.urls import path

from . import views


urlpatterns =[
    path('blogs/', views.BlogListView.as_view()),
    path('blog/create/', views.BlogCreateView.as_view()),
    path('blog/update/<int:pk>', views.BlogUpdateDeleteView.as_view()),
]
