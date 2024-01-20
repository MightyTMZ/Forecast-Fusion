from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ForecastSnapShot
from .serializers import ForecastSnapShotSerializer


class ForecastSnapshotList(APIView):
    def get(self, request, format=None):
        snapshots = ForecastSnapShot.objects.all()
        serializer = ForecastSnapShotSerializer(snapshots, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ForecastSnapShotSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()  # Save the data to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
