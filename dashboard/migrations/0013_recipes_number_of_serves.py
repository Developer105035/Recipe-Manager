# Generated by Django 3.2.5 on 2022-07-21 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20220721_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='number_of_serves',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
