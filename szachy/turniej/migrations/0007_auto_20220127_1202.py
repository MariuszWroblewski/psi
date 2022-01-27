# Generated by Django 3.2.9 on 2022-01-27 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('turniej', '0006_alter_turniej_nr_budynku'),
    ]

    operations = [
        migrations.AddField(
            model_name='rozgrywka',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mecz', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='turniej',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='turniej', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='turniej',
            name='data',
            field=models.DateField(null=True),
        ),
    ]
