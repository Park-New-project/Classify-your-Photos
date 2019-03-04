# Generated by Django 2.0.10 on 2019-03-04 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_photo_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='owner',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
