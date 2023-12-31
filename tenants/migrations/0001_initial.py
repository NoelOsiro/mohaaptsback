# Generated by Django 4.2.5 on 2023-09-21 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0001_initial'),
        ('properties', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='tenant_images/')),
                ('identification_pdf', models.FileField(blank=True, null=True, upload_to='tenant_identification/')),
                ('lease_agreement_pdf', models.FileField(blank=True, null=True, upload_to='tenant_lease_agreements/')),
                ('booking_date', models.DateTimeField(blank=True, null=True)),
                ('booked_property', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='properties.property')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateField()),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('unsolved', 'Unsolved'), ('resolved', 'Resolved')], default='pending', max_length=20)),
                ('completion_date', models.DateField(blank=True, null=True)),
                ('assigned_staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='staff.staff')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenants.tenant')),
            ],
        ),
    ]
