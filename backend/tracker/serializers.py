from rest_framework import serializers
from .models import Project
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "title", "description", "status", "due_date", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
    def validate_title(self, value):
        value = value.strip()
        if not value: raise serializers.ValidationError("Title cannot be blank.")
        return value
