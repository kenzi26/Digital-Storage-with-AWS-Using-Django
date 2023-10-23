from rest_framework import routers
from .views import DigialStorageViewSet


router = routers.DefaultRouter()

#Digtial Storage Endpoint
router.register(r'digtalupload',DigialStorageViewSet, basename="digtalupload")






urlpatterns = router.urls