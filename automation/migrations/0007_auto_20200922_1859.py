# Generated by Django 3.1 on 2020-09-22 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automation', '0006_auto_20200922_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productrequest',
            name='product_unit',
            field=models.CharField(max_length=50, verbose_name='واحد'),
        ),
    ]