from django.shortcuts import render
from .models import *
from .serializers import myDataSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
# Create your views here.


def Home(request):
    return render(request, 'appone/index.html')

# queryset is the model and the serializer class is the serializer name
# MAKING A POST REQUEST


class myDataView(generics.CreateAPIView):
    queryset = MyData.objects.all()
    serializer_class = myDataSerializer


class GetData(generics.ListAPIView):
    queryset = MyData.objects.all()
    serializer_class = myDataSerializer
