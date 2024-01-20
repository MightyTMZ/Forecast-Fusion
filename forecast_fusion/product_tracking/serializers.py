from rest_framework import serializers
from .models import FusionPod

class FusionPodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FusionPod
        fields = ['id', 'device_name', 'production_date', 'purchased_date']