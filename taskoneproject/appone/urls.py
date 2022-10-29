from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name="Home"),
    path('addData/', views.myDataView.as_view(), name="AddData"),
    path('getData/', views.GetData, name="GetData"),
    # path('getData/', views.GetData.as_view(), name="GetData"),
]
