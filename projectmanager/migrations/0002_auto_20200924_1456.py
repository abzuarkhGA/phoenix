# Generated by Django 3.1 on 2020-09-24 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projectmanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('priority', models.IntegerField(default=100, verbose_name='ترتیب')),
                ('image_header', models.ImageField(blank=True, null=True, upload_to='projectmanager/images/OurWorkCategory/', verbose_name='تصویر سربرگ')),
            ],
            options={
                'verbose_name': 'ProjectCategory',
                'verbose_name_plural': 'ProjectCategories',
            },
        ),
        migrations.AlterField(
            model_name='material',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='material_category', to='projectmanager.materialcategory'),
        ),
        migrations.AlterField(
            model_name='materialcategory',
            name='image_origin',
            field=models.ImageField(blank=True, null=True, upload_to='projectmanager/images/MaterialCategory/', verbose_name='تصویر'),
        ),
        migrations.CreateModel(
            name='WorkUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('حسابداری', 'حسابداری'), ('مدیریت', 'مدیریت'), ('حمل و نقل', 'حمل و نقل'), ('کارپردازی', 'کارپردازی'), ('عمران', 'عمران'), ('تاسیسات', 'تاسیسات'), ('مهندسی', 'مهندسی')], default='حسابداری', max_length=50, verbose_name='title')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='description')),
                ('employees', models.ManyToManyField(blank=True, to='projectmanager.Employee', verbose_name='نیروی انسانی')),
            ],
            options={
                'verbose_name': 'WorkUnit',
                'verbose_name_plural': 'WorkUnits',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pretitle', models.CharField(blank=True, max_length=500, null=True, verbose_name='پیش عنوان')),
                ('title', models.CharField(blank=True, max_length=500, null=True, verbose_name='عنوان')),
                ('posttitle', models.CharField(blank=True, max_length=500, null=True, verbose_name='پس عنوان')),
                ('short_description', models.TextField(blank=True, null=True, verbose_name='شرح کوتاه')),
                ('description', models.TextField(blank=True, null=True, verbose_name='شرح کامل')),
                ('action_text', models.CharField(blank=True, max_length=100, null=True, verbose_name='متن دکمه')),
                ('action_url', models.CharField(blank=True, max_length=2000, null=True, verbose_name='لینک دکمه')),
                ('video_text', models.CharField(blank=True, max_length=100, null=True, verbose_name='متن ویدیو')),
                ('video_url', models.CharField(blank=True, max_length=2000, null=True, verbose_name='لینک ویدیو')),
                ('location', models.CharField(blank=True, max_length=500, null=True, verbose_name='موقعیت در نقشه گوگل 400*400')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='projectmanager.projectcategory', verbose_name='category')),
                ('material_warehouses', models.ManyToManyField(blank=True, to='projectmanager.MaterialWareHouse', verbose_name='material_warehouses')),
                ('work_units', models.ManyToManyField(blank=True, to='projectmanager.WorkUnit', verbose_name='work_units')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
    ]