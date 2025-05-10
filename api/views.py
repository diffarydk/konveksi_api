# from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import ProdukPost
from .serializers import ProdukPostSerializers


# Create your views here.
class ProdukPostListCreate(generics.ListCreateAPIView):
    queryset = ProdukPost.objects.all()
    serializer_class = ProdukPostSerializers
    permission_classes = [IsAuthenticated]


class ProdukPostRetUpdateDel(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProdukPost.objects.all()
    serializer_class = ProdukPostSerializers
    lookup_field = "pk"
    permission_classes = [IsAuthenticated]
