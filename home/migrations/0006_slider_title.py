# Generated by Django 4.0.2 on 2022-03-14 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_slider'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
