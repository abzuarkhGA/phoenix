# Generated by Django 3.1 on 2020-09-29 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_resume_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='duration',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='مدت زمان'),
        ),
    ]
