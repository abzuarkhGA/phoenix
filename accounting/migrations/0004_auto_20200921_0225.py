# Generated by Django 3.1 on 2020-09-20 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200920_0550'),
        ('accounting', '0003_auto_20200920_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='financialyear',
            name='documents',
        ),
        migrations.AddField(
            model_name='financialdocument',
            name='documents',
            field=models.ManyToManyField(to='app.Document', verbose_name='فایل ها'),
        ),
        migrations.AddField(
            model_name='financialdocument',
            name='links',
            field=models.ManyToManyField(to='app.Link', verbose_name='لینک ها'),
        ),
    ]
