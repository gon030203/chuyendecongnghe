from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # function view
    path('about/', views.about, name='about'),  # function view
    path('contact/', views.ContactView.as_view(), name='contact'),  # class view
    path('posts/', views.PostListView.as_view(), name='post_list'),  # class view
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  # class view
]
