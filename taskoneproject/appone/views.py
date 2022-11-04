from django.shortcuts import render
from .models import *
from .serializers import myDataSerializer, FetchModelSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
from rest_framework.decorators import api_view
from django.http import JsonResponse

#
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status


@api_view(["POST"])
def Home(request, *args, **kwargs):
    header = {"Access-Control-Allow-Origin": "*"}
    info = request.data
    infoX = info['x']
    infoY = info['y']
    operator = info['operation_type']
    if (operator == 'subtraction'):
        solution = (infoX - infoY)
    elif (operator == 'addition'):
        solution = (infoX + infoY)
    elif (operator == 'multiplication'):
        solution = (infoX * infoY)
        data = {
            "slackUsername": "Isaac Franklin Tochukwu",
            "Operation": operator,
            "result": solution,
            # "bio": "I joined HNG9 to learn what exactly it takes to be a world-class developer"
        }
        return JsonResponse(data, headers=header, safe=False)
    return JsonResponse("Something went wrong: Please make sure your operator starts with a small letter (eg: addition not Addition)", headers=header, safe=False)

# class myDataView(generics.CreateAPIView):
#     queryset = MyData.objects.all()
#     serializer_class = myDataSerializer


# class GetData(generics.ListAPIView):
#     queryset = MyData.objects.all()
#     serializer_class = myDataSerializer


# tutorial_data = JSONParser().parse(request)
# tutorial_serializer = TutorialSerializer(data=tutorial_data)
# if tutorial_serializer.is_valid():
#     tutorial_serializer.save()
#     return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)


# @api_view(["POST"])
# def AddData(request):
#     fetchData = JSONParser().parse(request)
#     # apiInfo = FetchModel.save()
#     addDataSerializer = FetchModelSerializer(data=fetchData)
#     if addDataSerializer.is_valid():
#         addDataSerializer.save()
#         return JsonResponse(addDataSerializer.data, status=status.HTTP_201_CREATED)
#     # fetchserializer = FetchModelSerializer(apiInfo, many=True),
#     return JsonResponse(addDataSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def GetData(request):
    queryset = MyData.objects.get()
    serializer = myDataSerializer(queryset)
    return Response(serializer.data)
