# Generated by Django 2.2.4 on 2020-04-10 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='authorUserName',
            field=models.CharField(default='tad', max_length=16),
            preserve_default=False,
        ),
    ]