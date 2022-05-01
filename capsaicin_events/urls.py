from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from api.views import UserViewSet, EventViewSet
from api.auth import authenticate, register

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'user', UserViewSet)
router.register(r'event', EventViewSet)


urlpatterns = [
    path('admin/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/authenticate',
         authenticate,
         name='authenticate'),
    path('api/register',
         register,
         name='register'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
