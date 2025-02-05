from rest_framework import serializers
from app.models import Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
        read_only_fields = ('uuid', 'deleted_at', 'last_updated_at')