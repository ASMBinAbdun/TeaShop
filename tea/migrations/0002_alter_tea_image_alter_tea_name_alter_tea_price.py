# Generated by Django 4.2.11 on 2024-07-25 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tea', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tea',
            name='image',
            field=models.ImageField(upload_to='tea/'),
        ),
        migrations.AlterField(
            model_name='tea',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tea',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
