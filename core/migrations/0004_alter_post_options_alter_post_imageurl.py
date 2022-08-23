# Generated by Django 4.0.6 on 2022-08-22 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_post_comments_remove_post_likes_like_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['description']},
        ),
        migrations.AlterField(
            model_name='post',
            name='imageUrl',
            field=models.ImageField(default='post/images/pet-sitting-pg.jpg', upload_to='post/images'),
        ),
    ]