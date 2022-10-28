# Generated by Django 3.2.5 on 2022-07-21 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_utensils'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=100, null=True)),
                ('ingredient_id', models.PositiveIntegerField(null=True)),
            ],
        ),
    ]
