# Generated by Django 3.2.5 on 2021-07-26 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mtaa', '0014_auto_20210726_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='hood_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mtaa.neighbourhood'),
        ),
    ]
