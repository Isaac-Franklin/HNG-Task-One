from rest_framework import serializers
from .models import MyData
from .models import FetchModel


class myDataSerializer(serializers.Serializer):
    slackUsername = serializers.CharField()
    backend = serializers.BooleanField()
    age = serializers.IntegerField()
    bio = serializers.CharField()

    class Meta:
        model: MyData
        fields: ['SlackUserName', 'BackEnd', 'Age', 'Bio']

    # def create(self, validated_data):
    #     return super().create(validated_data)

    def create(self, validated_data):
        return MyData.objects.create(**validated_data)


# -----------------------------------------------------
class FetchModelSerializer(serializers.Serializer):
    operation_type = serializers.CharField()
    x = serializers.IntegerField()
    y = serializers.IntegerField()

    class Meta:
        model: FetchModel
        fields: ['operation_type', 'x', 'y']

    # def create(self, validated_data):
    #     return super().create(validated_data)

    # def create(self, validated_data):
    #     return FetchModel.objects.create(**validated_data)
