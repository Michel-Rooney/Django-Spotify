from rest_framework import viewsets
from .serializers import MusicSerializer
from django.shortcuts import render
from .models import Music


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer


def index(request):
    return render(request, 'pages/index.html')

