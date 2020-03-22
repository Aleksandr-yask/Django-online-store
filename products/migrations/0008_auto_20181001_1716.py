# Generated by Django 2.1.1 on 2018-10-01 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20181001_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='importance',
            field=models.CharField(choices=[('se', 'Secondary'), ('pr', 'Paramount')], default=1, max_length=2),
        ),
    ]