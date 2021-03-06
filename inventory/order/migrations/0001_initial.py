# Generated by Django 2.1.7 on 2019-03-15 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        ('product', '0003_auto_20190315_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tax', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('delivery_date', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_status', models.CharField(choices=[('cash', 'CASH'), ('credit', 'CREDIT')], max_length=30)),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='employee.Employee')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='order_lines',
            field=models.ManyToManyField(to='order.OrderLine'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product'),
        ),
    ]
