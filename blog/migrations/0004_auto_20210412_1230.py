# Generated by Django 3.1.7 on 2021-04-12 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210412_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]