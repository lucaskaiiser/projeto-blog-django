from django.urls import path
from blog.views import (
    index,
    post,
    page, 
    category, 
    tag, 
    created_by, 
    search
)
app_name = "blog"

urlpatterns = [
    path('', index, name="index"),
    path('post/<slug:slug>/',post, name='post'),
    path('category/<slug:slug>/',category, name='category'),
    path('tag/<slug:slug>/',tag, name='tag'),
    path('author/<int:id>/',created_by, name='author'),
    path('page/', page, name='page'),
    path('search/',search, name='search'),
]