# Generated by Django 4.1.6 on 2023-03-31 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_paciente_dni'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='dni',
            field=models.CharField(default='00000000', max_length=30),
        ),
    ]
