# Generated by Django 3.0.5 on 2020-04-30 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_finder', '0003_auto_20200430_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='amount',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
