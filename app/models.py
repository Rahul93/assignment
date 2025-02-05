import uuid
from django.db import models
from django.utils.timezone import now


class Location(models.Model):
    # Internal unique identifier
    location_code = models.CharField(max_length=10, unique=True)

    # UUID for external communication
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    code = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    coordinates = models.JSONField()
    timezone = models.CharField(max_length=50)
    unlocs = models.JSONField()
    alias = models.JSONField(default=list)
    regions = models.JSONField(default=list)

    # Soft delete field
    deleted_at = models.DateTimeField(null=True, blank=True)

    # Last updated timestamp
    last_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def is_deleted(self):
        """Check if the location is soft-deleted."""
        return self.deleted_at is not None

    def delete(self, *args, **kwargs):
        self.deleted_at = now()
        self.save(update_fields=['deleted_at'])

    def hard_delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
