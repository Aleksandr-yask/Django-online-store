# Generated by Django 2.1.1 on 2018-10-09 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_auto_20181004_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='img',
            field=models.CharField(blank=True, default=None, max_length=300),
        ),
        migrations.AddField(
            model_name='productinbasket',
            name='img',
            field=models.CharField(blank=True, default=None, max_length=300),
        ),
        migrations.AddField(
            model_name='productinorder',
            name='img',
            field=models.CharField(blank=True, default=None, max_length=300),
        ),
    ]