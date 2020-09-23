from rest_framework import serializers, viewsets
from .models import Render

class BlendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Render
        fields = ['inputPath', 'outputPath', 'reqDate']
