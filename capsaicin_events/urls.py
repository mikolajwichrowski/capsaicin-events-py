from django.urls import path, include
from rest_framework import routers

from api.views import UserViewSet, EventViewSet
from api.auth import authenticate, register

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'events', EventViewSet)


urlpatterns = [
    path('admin/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/authenticate',
         authenticate,
         name='authenticate'),
    path('api/register',
         register,
         name='register'),

]
