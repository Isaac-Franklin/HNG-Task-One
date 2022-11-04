from django.db import models
from .utils import choice_operation_type

# Create your models here.


class MyData(models.Model):
    slackUsername = models.CharField(max_length=200, null=True)
    backend = models.BooleanField(null=True)
    age = models.IntegerField(null=True)
    bio = models.CharField(max_length=1000, null=True)


class FetchModel(models.Model):

    # option = models.IntegerField(choices=Option.choices)
    # operation_type = models.IntegerField(choices=Option, null=True)
    # operation_type = models.IntegerField(
    #     choices=choice_operation_type.choices(), default=choice_operation_type.ADDITION)
    # x = models.IntegerField(null=True)
    # y = models.IntegerField(null=True)

    operation_type = models.CharField(max_length=200)
    x = models.IntegerField(null=True)
    y = models.IntegerField(null=True)

    # def get_FetchModel_label(self):
    #     return choice_operation_type(self.operation_type).name.title()
    # {
    #     "SlackUserName": "Franklin Isaac",
    #     "BackEnd": true,
    #     "Age": "26",
    #     "Bio": "I joined HNG9 to learn what exactly it takes to be a world-class developer"
    # }

    # class Suit(models.IntegerChoices):
    #     DIAMOND = 1
    #     SPADE = 2
    #     HEART = 3
    #     CLUB = 4

    # suit = models.IntegerField(choices=Suit.choices)
