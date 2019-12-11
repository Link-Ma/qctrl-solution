# Generated by Django 3.0 on 2019-12-08 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Control',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='no_name', max_length=100, verbose_name='name')),
                ('type', models.CharField(default='Primitive', max_length=50, verbose_name='type')),
                ('maximum_rabi_rate', models.FloatField()),
                ('polar_angle', models.FloatField()),
            ],
        ),
    ]
