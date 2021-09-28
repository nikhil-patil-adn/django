# Generated by Django 3.2.5 on 2021-08-18 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0006_auto_20210818_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Customertest',
        ),
        migrations.DeleteModel(
            name='Stafftest',
        ),
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('place_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='feedbacks.place')),
                ('serves_pizza', models.BooleanField(default=False)),
                ('serves_pasta', models.BooleanField(default=False)),
            ],
            bases=('feedbacks.place',),
        ),
    ]
