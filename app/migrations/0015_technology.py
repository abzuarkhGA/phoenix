# Generated by Django 3.1 on 2020-09-26 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20200927_0119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.page')),
            ],
            options={
                'verbose_name': 'Technology',
                'verbose_name_plural': 'تکنولوژی',
            },
            bases=('app.page',),
        ),
    ]
