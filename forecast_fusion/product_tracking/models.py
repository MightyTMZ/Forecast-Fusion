import uuid
from users.models import CustomUser
from django.db import models

# we create these models to store information of manufactured products


class FusionPod(models.Model):
    # user = models.ForeignKey(CustomUser, on_delete=models.PROTECT)
    id = models.UUIDField(
         primary_key=True,
         default=uuid.uuid4,
         editable=False)
    device_name = models.CharField(max_length=60, default=f"Device {id}")
    production_date = models.DateField(auto_now_add=True) # set upon production
    purchased_date = models.DateField(null=True, blank=True) # could be blank if not purchased yet
    
    def __str__(self) -> str:
        return f"{self.device_name}"
