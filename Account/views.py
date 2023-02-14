from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model


from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny


# Create your views here.
# class RegisterAPI(generics.GenericAPIView):
#     serializer_class = RegisterSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         return Response({
#         "user": UserSerializer(user, context=self.get_serializer_context()).data,
#         "token": AuthToken.objects.create(user)[1]
#         })


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    

class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)