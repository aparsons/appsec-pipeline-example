from rest_framework import serializers

from . import models


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Application
