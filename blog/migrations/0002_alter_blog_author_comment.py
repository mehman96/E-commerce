# Generated by Django 4.0.2 on 2022-02-18 07:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author_comment',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
