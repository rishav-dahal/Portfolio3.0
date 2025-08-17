from rest_framework import serializers
from blog.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'  
    )
    
    # Show tag names instead of IDs
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = BlogPost
        fields = [
            'id', 'title', 'slug', 'content', 'cover_image',
            'is_published', 'published_at', 'created_at',
            'categories', 'tags'
        ]


class BlogPostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields ="__all__"

    def validate(self, data):
        if not data.get('title'):
            raise serializers.ValidationError("Title is required.")
        if not data.get('content'):
            raise serializers.ValidationError("Content is required.")
        
        if not data.get('categories'):
            raise serializers.ValidationError("At least one category is required.")
        return data

    def create(self, validated_data):
        # Pop M2M fields from validated_data
        categories = validated_data.pop('categories', [])
        tags = validated_data.pop('tags', [])
        
        # Create the BlogPost instance
        blog_post = BlogPost.objects.create(**validated_data)
        
        # Add M2M relationships
        if categories:
            blog_post.categories.set(categories)
        if tags:
            blog_post.tags.set(tags)
            
        return blog_post

