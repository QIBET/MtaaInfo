# Generated by Django 3.2.5 on 2021-07-25 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtaa', '0004_neighbourhood_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contact',
            field=models.CharField(max_length=40, null=True),
        ),
    ]