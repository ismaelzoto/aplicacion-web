# Generated by Django 2.1.1 on 2018-09-26 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_alumnos', '0004_auto_20180925_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='nocontrol',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
