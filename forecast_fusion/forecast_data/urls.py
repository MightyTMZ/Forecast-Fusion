from .views import *
from django.urls import path


urlpatterns = [
    path("records/", ForecastSnapshotList.as_view(), name="forcast_data_list"),
]