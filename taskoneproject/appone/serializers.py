from rest_framework import serializers
from .models import MyData


class myDataSerializer(serializers.Serializer):

    SlackUserName = serializers.CharField()
    BackEnd = serializers.BooleanField()
    Age = serializers.IntegerField()
    Bio = serializers.CharField()

    class Meta:
        model: MyData
        fields: ['SlackUserName', 'BackEnd', 'Age', 'Bio']

    # def create(self, validated_data):
    #     return super().create(validated_data)

    def create(self, validated_data):
        return MyData.objects.create(**validated_data)
