# Generated by Django 3.2.5 on 2021-07-19 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('societymasters', '0001_initial'),
        ('customers', '0004_remove_customer_society'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='society',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='societymasters.societymaster'),
        ),
    ]
