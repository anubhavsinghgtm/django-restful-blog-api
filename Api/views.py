from rest_framework import generics
from Base.models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.permissions import IsAdminUser, DjangoModelPermissions, BasePermission, SAFE_METHODS,DjangoModelPermissionsOrAnonReadOnly


class PostUserWritePermission(BasePermission):
    message = "Editing the post is restricted to the author only."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user    # true, if the author is requested


class PostList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = BlogPost.postObject.all()
    serializer_class = BlogPostSerializer
    




class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = BlogPost.postObject.all()
    serializer_class = BlogPostSerializer
    
