# Generated by Django 2.1 on 2018-10-02 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0006_auto_20181003_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='items_type',
            field=models.CharField(choices=[('Bl', 'Blouse'), ('Sh', 'Shirt'), ('Sk', 'Skirt'), ('Gn', 'Gown')], default='Skirts', max_length=1),
        ),
    ]