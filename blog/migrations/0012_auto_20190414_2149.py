# Generated by Django 2.1.7 on 2019-04-14 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190414_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='phonenumber',
            field=models.TextField(blank=True, max_length=12, null=True),
        ),
    ]
