# Generated by Django 2.2.4 on 2020-04-25 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_post_thread'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
