# Generated by Django 4.0 on 2021-12-25 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutteam',
            old_name='commenter_desc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='aboutteam',
            old_name='commenter_fb_url',
            new_name='fb_url',
        ),
        migrations.RenameField(
            model_name='aboutteam',
            old_name='commenter_header',
            new_name='header',
        ),
        migrations.RenameField(
            model_name='aboutteam',
            old_name='commenter_instagram_url',
            new_name='instagram_url',
        ),
        migrations.RenameField(
            model_name='aboutteam',
            old_name='commenter_twitter_url',
            new_name='twitter_url',
        ),
    ]
