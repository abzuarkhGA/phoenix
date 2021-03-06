# Generated by Django 3.1 on 2020-09-22 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20200922_0912'),
        ('automation', '0005_auto_20200922_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='automationprofile', to='app.profile', verbose_name='profile'),
        ),
        migrations.AlterField(
            model_name='productrequest',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='automation.employee', verbose_name='employee'),
        ),
    ]
