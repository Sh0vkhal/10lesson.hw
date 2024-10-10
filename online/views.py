from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

# Create your views here.
from .models import  Video
from .serializer import FileSerializer



class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = FileSerializer
       