from rest_framework import generics
from Base.models import BlogPost
from .serializers import BlogPostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = BlogPost.postObject.all()
    serializer_class = BlogPostSerializer
    pass




class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = BlogPost.postObject.all()
    serializer_class = BlogPostSerializer
    pass
