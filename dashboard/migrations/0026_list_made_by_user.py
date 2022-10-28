# Generated by Django 3.2.5 on 2022-08-12 23:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0025_shared_recipes'),
    ]

    operations = [
        migrations.CreateModel(
            name='list_made_by_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_name', models.CharField(choices=[('seconds', 'seconds'), ('minutes', 'minutes'), ('hours', 'hours')], max_length=200, null=True)),
                ('recipe_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.recipes')),
                ('user_id', models.ForeignKey(db_column='user_id', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
