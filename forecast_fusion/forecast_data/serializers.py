from rest_framework import serializers
from .models import ForecastSnapShot
from product_tracking.serializers import FusionPodSerializer

class ForecastSnapShotSerializer(serializers.ModelSerializer):
    device = FusionPodSerializer()
    class Meta:
        model = ForecastSnapShot
        fields = ['device', 'timestamp', 'temperature_celsius', 'humidity']
