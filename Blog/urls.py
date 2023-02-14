
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from Account.views import UserViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Base.urls')),
    path('api/', include('Api.urls')),
    path('api/account/', include('Account.urls')),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


router = DefaultRouter()
router.register('user', UserViewSet,basename='user')


urlpatterns += router.urls