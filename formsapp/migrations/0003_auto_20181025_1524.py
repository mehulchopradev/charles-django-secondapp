# Generated by Django 2.1.1 on 2018-10-25 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formsapp', '0002_auto_20181025_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisheddate',
            field=models.DateField(blank=True, null=True),
        ),
    ]