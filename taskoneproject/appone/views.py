from django.shortcuts import render
from .models import *
from .serializers import myDataSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
from rest_framework.decorators import api_view
from django.http import JsonResponse


# def Home(request):
#     return render(request, 'appone/index.html')


@api_view(["GET"])
def Home(request, *args, **kwargs):
    header = {"Access-Control-Allow-Origin": "*"}
    data = {
        "slackUsername": "Isaac Franklin Tochukwu",
        "backend": True,
        "age": 26,
        "bio": "I joined HNG9 to learn what exactly it takes to be a world-class developer"
    }
    return JsonResponse(data, headers=header)
# def Home(request):
#     return render(request, 'appone/index.html')

# queryset is the model and the serializer class is the serializer name
# MAKING A POST REQUEST


class myDataView(generics.CreateAPIView):
    queryset = MyData.objects.all()
    serializer_class = myDataSerializer


# class GetData(generics.ListAPIView):
#     queryset = MyData.objects.all()
#     serializer_class = myDataSerializer

@api_view(["GET"])
def GetData(request):
    queryset = MyData.objects.get()
    serializer = myDataSerializer(queryset)
    return Response(serializer.data)
