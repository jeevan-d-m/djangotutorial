# Generated by Django 4.2.19 on 2025-03-01 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_product_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent_category_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category'),
        ),
    ]
