# Generated by Django 2.1 on 2018-10-03 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecom', '0014_auto_20181003_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=70)),
                ('billing_addr', models.CharField(max_length=500)),
                ('shipping_addr', models.CharField(max_length=500)),
                ('pincode', models.IntegerField(max_length=8)),
                ('phone_num', models.IntegerField(max_length=15)),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom.Cart')),
                ('products', models.ManyToManyField(blank=True, to='ecom.Products')),
            ],
        ),
        migrations.CreateModel(
            name='Specifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blouse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom.Blouse')),
                ('gowns', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom.Gowns')),
                ('products', models.ManyToManyField(blank=True, to='ecom.Products')),
                ('shirts', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom.Shirts')),
                ('skirts', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom.Skirts')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='billing',
            name='specifications',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom.Specifications'),
        ),
        migrations.AddField(
            model_name='billing',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
