# Generated by Django 2.2.4 on 2020-10-22 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spicyapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(related_name='comment_like', to='spicyapp.User'),
        ),
    ]