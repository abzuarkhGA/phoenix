# Generated by Django 3.1 on 2020-09-28 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20200928_0225'),
    ]

    operations = [
        migrations.AddField(
            model_name='partialpage',
            name='album',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.galleryalbum', verbose_name='آلبوم تصاویر'),
        ),
    ]
