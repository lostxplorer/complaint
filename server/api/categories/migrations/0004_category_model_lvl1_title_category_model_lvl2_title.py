# Generated by Django 4.1.7 on 2023-02-21 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_category_model_created_at_category_model_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='category_model',
            name='lvl1_title',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='category_model',
            name='lvl2_title',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
