from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from app.models import Location
from app.serializers import LocationSerializer

class LocationListCreateView(APIView):
    """
    API endpoint to list all locations or create a new location.
    """

    def get(self, request):
        """
        List all locations.
        Optionally include soft-deleted records using the `include_deleted` query parameter.
        """
        include_deleted = request.query_params.get('include_deleted', '').lower() == 'true'
        if include_deleted:
            locations = Location.objects.all()
        else:
            locations = Location.objects.filter(deleted_at__isnull=True)

        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    def post(self, request):
        """
        Create a new location.
        """
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocationDetailView(APIView):
    """
    API endpoint to retrieve, update, or soft-delete a specific location by its `uuid`.
    """

    def get_object(self, uuid):
        """
        Retrieve a location by its `uuid`.
        Exclude soft-deleted records by default.
        """
        try:
            return Location.objects.get(uuid=uuid, deleted_at__isnull=True)
        except Location.DoesNotExist:
            raise Http404

    def get(self, request, uuid):
        """
        Retrieve a specific location by `uuid`.
        """
        location = self.get_object(uuid)
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    def put(self, request, uuid):
        """
        Update a specific location by `uuid`.
        """
        location = self.get_object(uuid)
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid):
        """
        Soft-delete a specific location by `uuid`.
        """
        location = self.get_object(uuid)
        location.delete()  # Calls the overridden `delete` method for soft deletion
        return Response(status=status.HTTP_204_NO_CONTENT)