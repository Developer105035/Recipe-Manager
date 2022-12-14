# Generated by Django 3.2.5 on 2022-07-21 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_keywords'),
    ]

    operations = [
        migrations.CreateModel(
            name='process_steps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_id', models.PositiveIntegerField(null=True)),
                ('step_no', models.PositiveIntegerField(null=True)),
                ('utensil_id', models.PositiveIntegerField(null=True)),
                ('ingredient_id', models.PositiveIntegerField(null=True)),
                ('temperature', models.PositiveIntegerField(null=True)),
                ('time', models.PositiveIntegerField(null=True)),
            ],
        ),
    ]
