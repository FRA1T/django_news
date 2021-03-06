# Generated by Django 3.1.2 on 2020-11-04 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('news', '0001_initial'),
        ('comments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='postcommentmodel',
            name='comment_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to=settings.AUTH_USER_MODEL, verbose_name='Comment author'),
        ),
        migrations.AddField(
            model_name='postcommentmodel',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='comments.postcommentmodel', verbose_name='Parent comment'),
        ),
        migrations.AddField(
            model_name='postcommentmodel',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='news.postmodel', verbose_name='Post'),
        ),
    ]
