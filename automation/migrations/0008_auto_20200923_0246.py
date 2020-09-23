# Generated by Django 3.1 on 2020-09-22 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0004_auto_20200918_0237'),
        ('automation', '0007_auto_20200922_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productrequest',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='automation.employee', verbose_name='پرسنل'),
        ),
        migrations.AlterField(
            model_name='productrequest',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='market.product', verbose_name='کالا'),
        ),
        migrations.AlterField(
            model_name='productrequest',
            name='purchase_agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='automation.purchaseagent', verbose_name='مسئول خرید'),
        ),
        migrations.AlterField(
            model_name='productrequest',
            name='quantity',
            field=models.IntegerField(verbose_name='تعداد'),
        ),
        migrations.AlterField(
            model_name='productrequest',
            name='signatures',
            field=models.ManyToManyField(blank=True, to='automation.ProductRequestSignature', verbose_name='امضا ها'),
        ),
        migrations.AlterField(
            model_name='productrequest',
            name='status',
            field=models.CharField(choices=[('پذیرفته شده', 'پذیرفته شده'), ('رد شده', 'رد شده'), ('درخواست شده', 'درخواست شده'), ('در حال انجام', 'در حال انجام'), ('در حال پردازش', 'در حال پردازش'), ('لغو شده', 'لغو شده'), ('کامل شده', 'کامل شده')], default='درخواست شده', max_length=50, verbose_name='وضعیت'),
        ),
    ]
