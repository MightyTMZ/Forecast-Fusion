from django.db import models
from product_tracking.models import FusionPod


class ForecastSnapShot(models.Model):
    device = models.ForeignKey(FusionPod, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    temperature_celsius = models.FloatField()
    humidity = models.FloatField()
