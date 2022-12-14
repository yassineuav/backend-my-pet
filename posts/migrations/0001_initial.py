# Generated by Django 4.0.6 on 2022-08-05 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('like_post_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_from', models.CharField(choices=[('A', 'Android'), ('I', 'Iphone'), ('W', 'WebApp')], default='W', max_length=1)),
                ('content_type', models.CharField(choices=[('I', 'image'), ('V', 'video')], default='I', max_length=1)),
                ('description', models.TextField()),
                ('imageUrl', models.ImageField(default='', upload_to='post/images')),
                ('usersIn', models.IntegerField(default=0)),
                ('suggestedTimes', models.IntegerField(default=0)),
                ('display', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('likes_count', models.IntegerField(default=0)),
                ('comments', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.comments')),
                ('likes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.like')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=255)),
                ('full_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('imageUrl', models.ImageField(default='profile/avatar_female.jpg', upload_to='profile')),
            ],
        ),
        migrations.CreateModel(
            name='Views',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viewed_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.user')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=255)),
                ('suggestedTimes', models.IntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.user')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.user'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.user'),
        ),
    ]
