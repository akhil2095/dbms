# Generated by Django 2.0.6 on 2018-06-27 17:33

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0003_auto_20180627_1829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course',
        ),
        migrations.RemoveField(
            model_name='course',
            name='id',
        ),
        migrations.RemoveField(
            model_name='course',
            name='student',
        ),
        migrations.AddField(
            model_name='course',
            name='auto_increment_id',
            field=models.AutoField(default=django.utils.timezone.now, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='course_offered',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='course',
            field=models.CharField(default='', max_length=200),
        ),
    ]
