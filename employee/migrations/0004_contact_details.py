# Generated by Django 5.1.6 on 2025-02-25 13:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.BigIntegerField()),
                ('address', models.CharField(max_length=200)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
            ],
        ),
    ]
