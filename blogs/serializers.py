from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    """
    Serializer for Blog model.
    Converts Blog instances to JSON and validates incoming data.
    """
    class Meta:
        model = Blog
        fields = '__all__' # Returns all fields from the Blog model
