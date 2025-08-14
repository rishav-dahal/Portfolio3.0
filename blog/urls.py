from django.urls import path
from blog.views import list_blogs, create_blog

urlpatterns = [
    path('list-blogs/', list_blogs, name='list_blogs'),
    path('create-blog/', create_blog, name='create_blog'),
    
]
