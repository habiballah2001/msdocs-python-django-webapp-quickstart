# Generated by Django 4.2.1 on 2023-05-25 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_alter_discount_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.discount'),
        ),
    ]
