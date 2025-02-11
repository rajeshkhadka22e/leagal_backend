# Generated by Django 5.1.6 on 2025-02-11 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_remove_teammember_is_list_item_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teammember',
            options={'ordering': ['number'], 'verbose_name': 'Team Member', 'verbose_name_plural': 'Team Members'},
        ),
        migrations.AddField(
            model_name='teammember',
            name='number',
            field=models.IntegerField(default=0, verbose_name='Order Number'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.CharField(max_length=255),
        ),
    ]
