# Generated by Django 3.1 on 2020-10-07 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0044_auto_20201007_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialinstock',
            name='date_opi',
            field=models.DateTimeField(blank=True, null=True, verbose_name='تاریخ opi'),
        ),
    ]