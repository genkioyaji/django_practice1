# Generated by Django 2.0.7 on 2020-02-24 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200224_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
