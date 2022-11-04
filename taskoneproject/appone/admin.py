from django.contrib import admin
from .models import MyData
from .models import FetchModel
# Register your models here.
admin.site.register(FetchModel)
admin.site.register(MyData)
