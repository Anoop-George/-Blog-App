# Generated by Django 2.1.7 on 2019-04-13 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190412_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=2000),
        ),
    ]
