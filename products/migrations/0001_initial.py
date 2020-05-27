# Generated by Django 3.0.6 on 2020-05-12 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('ingrediants', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Cakes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('size', models.CharField(max_length=255)),
                ('toping', models.CharField(max_length=255)),
                ('weight', models.FloatField()),
                ('base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Base')),
            ],
        ),
    ]
