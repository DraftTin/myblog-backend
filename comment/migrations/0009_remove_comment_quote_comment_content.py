# Generated by Django 3.1.7 on 2021-04-21 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0008_auto_20210421_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='quote_comment_content',
        ),
    ]