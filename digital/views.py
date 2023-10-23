from rest_framework import viewsets,filters
from .models import DigitalStorage
from .serializers import DigitalStorageSerializer

class DigialStorageViewSet(viewsets.ModelViewSet):
    queryset = DigitalStorage.objects.all()
    serializer_class = DigitalStorageSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('image__file', 'video__file', 'music__file', 'document_file', 'user' )