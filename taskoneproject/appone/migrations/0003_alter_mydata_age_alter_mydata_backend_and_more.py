# Generated by Django 4.0.5 on 2022-10-27 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0002_mydata_age_mydata_backend_mydata_slackusername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mydata',
            name='Age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='mydata',
            name='BackEnd',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='mydata',
            name='Bio',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='mydata',
            name='SlackUserName',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
