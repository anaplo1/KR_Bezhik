# Generated by Django 4.1.3 on 2022-11-03 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_keeper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completeddiscipline',
            name='mark',
            field=models.TextField(),
        ),
    ]
