# Generated by Django 3.1 on 2020-09-29 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_auto_20200930_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeslider',
            name='text_color',
            field=models.CharField(default='#fff', max_length=20, verbose_name='رنگ متن'),
        ),
    ]