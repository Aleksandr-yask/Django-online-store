# Generated by Django 2.1.1 on 2018-10-02 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20181001_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='importance',
            field=models.CharField(choices=[('2', 'Secondary'), ('1', 'Paramount')], default=1, max_length=2),
        ),
    ]
