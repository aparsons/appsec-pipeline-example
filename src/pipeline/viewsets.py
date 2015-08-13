from rest_framework import viewsets

from . import models, serializers


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = models.Application.objects.all()
    serializer_class = serializers.ApplicationSerializer
