# Generated by Django 2.1 on 2018-10-02 20:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0004_remove_products_uploaded_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('half_length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ub_length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ub_width', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sleeve', models.DecimalField(decimal_places=2, max_digits=10)),
                ('round_sleeve', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tf_sleeve', models.DecimalField(decimal_places=2, max_digits=10)),
                ('long_sleeve', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shoulder', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Gowns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('short_length', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Shirts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('half_length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ub_length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ub_width', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sleeve', models.DecimalField(decimal_places=2, max_digits=10)),
                ('round_sleeve', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tf_sleeve', models.DecimalField(decimal_places=2, max_digits=10)),
                ('long_sleeve', models.DecimalField(decimal_places=2, max_digits=10)),
                ('shoulder', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Skirts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.DecimalField(decimal_places=2, max_digits=10)),
                ('height', models.DecimalField(decimal_places=2, max_digits=10)),
                ('length', models.DecimalField(decimal_places=2, max_digits=10)),
                ('knee_length', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='item_type',
            field=models.CharField(choices=[('Bl', 'Blouse'), ('Sh', 'Shirt'), ('Sk', 'Skirt'), ('Gn', 'Gown')], default=django.utils.timezone.now, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='skirts',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.Products'),
        ),
        migrations.AddField(
            model_name='shirts',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.Products'),
        ),
        migrations.AddField(
            model_name='gowns',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.Products'),
        ),
        migrations.AddField(
            model_name='blouse',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.Products'),
        ),
    ]
