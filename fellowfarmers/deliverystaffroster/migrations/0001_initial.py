# Generated by Django 3.2.5 on 2021-07-20 07:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staffpersons', '0005_alter_staffperson_pincode'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryStaffRoster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendace_status', models.CharField(choices=[('present', 'Present'), ('absent', 'Absent')], max_length=200)),
                ('date_of_attendance', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staffpersons.staffperson')),
            ],
        ),
    ]