# Generated by Django 4.2 on 2023-05-02 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0013_product'),
        ('accounts', '0002_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField()),
                ('phone', models.CharField(max_length=20)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to='accounts.city')),
                ('product_favorites', models.ManyToManyField(to='products.product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
