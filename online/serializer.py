from rest_framework import serializers
from .models import Video

class FileSerializer(serializers.Serializer):
    class Meta:
        model = Video
        fields = '__all__'
        read_only_fields = ('created_at')


