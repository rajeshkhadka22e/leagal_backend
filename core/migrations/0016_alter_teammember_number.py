# Generated by Django 5.1.6 on 2025-02-11 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_teammember_options_teammember_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='number',
            field=models.IntegerField(default=20, verbose_name='Order Number'),
        ),
    ]
