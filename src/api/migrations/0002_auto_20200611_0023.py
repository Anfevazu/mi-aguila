# Generated by Django 3.0.6 on 2020-06-11 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='created',
            field=models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', null=True, verbose_name='created at'),
        ),
        migrations.AddField(
            model_name='trip',
            name='modified',
            field=models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', null=True, verbose_name='modified at'),
        ),
    ]
