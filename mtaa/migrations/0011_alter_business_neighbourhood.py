# Generated by Django 3.2.5 on 2021-07-26 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mtaa', '0010_alter_post_neighbourhood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='neighbourhood',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mtaa.neighbourhood'),
            preserve_default=False,
        ),
    ]
