# Generated by Django 3.1.3 on 2020-11-30 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languages',
            name='langs',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]