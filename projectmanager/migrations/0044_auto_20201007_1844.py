# Generated by Django 3.1 on 2020-10-07 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0043_auto_20201007_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='model',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='model'),
        ),
        migrations.AlterField(
            model_name='material',
            name='unit_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='واحد'),
        ),
    ]
