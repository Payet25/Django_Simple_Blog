# Generated by Django 4.0.2 on 2022-02-06 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheBlog', '0008_remove_post_likes_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='To Keiren', max_length=255),
        ),
    ]