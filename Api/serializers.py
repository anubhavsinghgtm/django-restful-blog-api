from rest_framework import serializers
from Base.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'author', 'body', 'created_at', 'published')
