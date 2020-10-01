# Generated by Django 3.1 on 2020-10-01 19:48

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0031_auto_20200930_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managerpage',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='شرح کامل'),
        ),
        migrations.AlterField(
            model_name='managerpage',
            name='short_description',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='شرح کوتاه'),
        ),
    ]
