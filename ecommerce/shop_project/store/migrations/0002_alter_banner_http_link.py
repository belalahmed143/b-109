# Generated by Django 3.2.15 on 2022-12-07 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='http_link',
            field=models.URLField(blank=True, max_length=400, null=True),
        ),
    ]