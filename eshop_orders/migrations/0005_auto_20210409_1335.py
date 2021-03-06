# Generated by Django 3.2 on 2021-04-09 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_product', '0002_alter_product_price'),
        ('eshop_orders', '0004_order_total_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderdetail',
            name='price',
        ),
        migrations.CreateModel(
            name='OrderPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('count', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relpay', to='eshop_orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop_product.product')),
            ],
        ),
    ]
