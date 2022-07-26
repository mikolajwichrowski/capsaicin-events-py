from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from api.views import UserViewSet, EventViewSet
from api.auth import authenticate, register
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Capsacin events py",
      default_version='v1',
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


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
     path("swagger.json", schema_view.without_ui(cache_timeout=0), name='schema-json'),
     path("swagger/index.html", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
