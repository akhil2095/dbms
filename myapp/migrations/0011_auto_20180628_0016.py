# Generated by Django 2.0.6 on 2018-06-27 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20180628_0012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_offered',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]
