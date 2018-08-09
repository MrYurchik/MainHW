# Generated by Django 2.0.6 on 2018-08-09 10:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0005_auto_20180803_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='ПОСТ')),
                ('new', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.News', verbose_name='ПОСТ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name="PolsoBatel'")),
            ],
            options={
                'verbose_name': 'ПОСТ',
                'verbose_name_plural': 'ПОСТЫ',
            },
        ),
    ]
