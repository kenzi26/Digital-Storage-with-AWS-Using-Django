from django.contrib import admin
from django.urls import path, include, re_path

# DRF YASG Imports
from django.urls import re_path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers, permissions
from drf_yasg import openapi
from django.conf.urls.static import static
from django.conf import settings


router = routers.DefaultRouter()
urlpatterns = router.urls


schema_view = get_schema_view(
   openapi.Info(
      title="KEEP-AM-HERE API",
      default_version='v1',
      description="Description Of API DOCs",
      contact=openapi.Contact(email="mokwenyekene1@yahoo.com"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns += [
    path('', include('admin_volt.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('api/physical-storage/', include('physical_storage.urls')),
    path('api/digital/', include('digital.urls')),

    re_path(
        r"^api/docs/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]



  

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)