# Generated by Django 3.1 on 2020-09-29 21:48

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20200930_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jumbotron',
            name='description',
            field=tinymce.models.HTMLField(blank=True, max_length=2000, null=True, verbose_name='شرح کامل'),
        ),
        migrations.AlterField(
            model_name='jumbotron',
            name='short_description',
            field=tinymce.models.HTMLField(blank=True, max_length=1000, null=True, verbose_name='شرح کوتاه'),
        ),
    ]
