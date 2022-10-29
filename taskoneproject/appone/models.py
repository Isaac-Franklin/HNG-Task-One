from django.db import models

# Create your models here.


class MyData(models.Model):
    slackUsername = models.CharField(max_length=200, null=True)
    backend = models.BooleanField(null=True)
    age = models.IntegerField(null=True)
    bio = models.CharField(max_length=1000, null=True)


# {
#     "SlackUserName": "Franklin Isaac",
#     "BackEnd": true,
#     "Age": "26",
#     "Bio": "I joined HNG9 to learn what exactly it takes to be a world-class developer"
# }
