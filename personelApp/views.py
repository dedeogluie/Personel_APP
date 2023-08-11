from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .permissions import IsStaffOrReadOnly

from .models import Departman ,Personel
from .serializers import DepartmanSerializer,PersonelSerializer

class DepartmanView(ModelViewSet):
    queryset = Departman.objects.all()
    serializer_class = DepartmanSerializer
    # permission_classes = [IsStaffOrReadOnly]
    permission_classes = [IsAuthenticated, IsStaffOrReadOnly]
    
class PersonelView(ModelViewSet):
    queryset = Personel.objects.all()
    serializer_class= PersonelSerializer
    permission_classes = [IsAuthenticated, IsStaffOrReadOnly]
