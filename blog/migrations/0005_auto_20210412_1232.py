# Generated by Django 3.1.7 on 2021-04-12 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210412_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='registered',
            field=models.DateField(auto_now=True),
        ),
    ]