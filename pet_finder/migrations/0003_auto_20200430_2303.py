# Generated by Django 3.0.5 on 2020-04-30 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet_finder', '0002_auto_20200430_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='amount',
            field=models.PositiveIntegerField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='reward',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
