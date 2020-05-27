# Generated by Django 3.0.6 on 2020-05-12 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=2083)),
                ('discount', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='cakes',
            name='image_url',
            field=models.CharField(default='defult.jpg', max_length=2083),
        ),
        migrations.AlterField(
            model_name='base',
            name='name',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='cakes',
            name='price',
            field=models.FloatField(),
        ),
    ]
