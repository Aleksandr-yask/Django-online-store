# Generated by Django 2.1.1 on 2018-10-09 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_auto_20181009_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinbasket',
            name='img',
            field=models.CharField(blank=True, default=None, max_length=300, null=True),
        ),
    ]
