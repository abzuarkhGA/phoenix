# Generated by Django 3.1 on 2020-10-05 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0040_auto_20201005_1248'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialinstock',
            name='unit_name',
            field=models.CharField(default='عدد', max_length=50, verbose_name='واحد'),
            preserve_default=False,
        ),
    ]
