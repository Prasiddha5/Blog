from django.urls import path
from .views import BlogListCreateView, BlogRetrieveUpdateView

urlpatterns = [
     # List + Create Blogs
    path('', BlogListCreateView.as_view(), name='blog-list-create'),
     # Retrieve + Update Blog by ID
    path('<int:pk>/', BlogRetrieveUpdateView.as_view(), name='blog-detail'),
]
