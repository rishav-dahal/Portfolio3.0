from django.urls import path
from blog.views import list_blogs, create_blog, update_blog

urlpatterns = [
    path('list-blogs/', list_blogs, name='list_blogs'),
    path('create-blog/', create_blog, name='create_blog'),
    path('update-blog/<str:slug>/', update_blog, name='update_blog'),
    
]
