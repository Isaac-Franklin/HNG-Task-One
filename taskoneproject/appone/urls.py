from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('addData/', views.Home, name="AddData"),
    # path('addData/', views.myDataView.as_view(), name="AddData"),
    path('getData/', views.GetData, name="GetData"),
    # path('addData/', views.AddData, name="AddData"),
]
