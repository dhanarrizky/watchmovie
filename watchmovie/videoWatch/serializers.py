from .models import Video
from rest_framework import serializers

class videoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id','file','description']
    