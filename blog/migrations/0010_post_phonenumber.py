# Generated by Django 2.1.7 on 2019-04-14 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190413_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='phonenumber',
            field=models.IntegerField(max_length=12, null=True),
        ),
    ]
