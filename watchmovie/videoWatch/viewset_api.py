from .models import Video
from .serializers import videoSerializer
from rest_framework import viewsets, permissions

class videoViewsets(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = videoSerializer
    permission_classes = [permissions.IsAuthenticated]
