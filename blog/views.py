from django.shortcuts import render
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import BlogPost 
from blog.serializers import BlogPostSerializer , BlogPostCreateSerializer
from rest_framework import serializers


@api_view(["GET"])
def list_blogs(request):
    try:
        query = BlogPost.objects.all()
        serializer = BlogPostSerializer(query, many=True)
        status_code = status.HTTP_200_OK if query else status.HTTP_204_NO_CONTENT
        return Response(status=status_code , data=serializer.data)
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, message="An error occurred while fetching blog posts: ")


@api_view(["POST"])
def create_blog(request):
    try:
        serializer = BlogPostCreateSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True): 
            return Response(status=status.HTTP_400_BAD_REQUEST,message="Invalid data")
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=BlogPostSerializer(serializer.instance).data)   
    except serializers.ValidationError as e:
        return Response(status=status.HTTP_400_BAD_REQUEST, data={"error": str(e)})
    except Exception as e:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR, message="An error occurred while creating the blog post: ")