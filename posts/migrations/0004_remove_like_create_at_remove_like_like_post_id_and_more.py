# Generated by Django 4.0.6 on 2022-08-05 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_post_create_at_remove_post_imageurl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='create_at',
        ),
        migrations.RemoveField(
            model_name='like',
            name='like_post_id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, to='posts.like'),
        ),
    ]