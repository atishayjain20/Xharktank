# Generated by Django 3.2.3 on 2022-04-06 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Xharktanks', '0004_auto_20220406_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entre',
            name='offers',
            field=models.ManyToManyField(blank=True, to='Xharktanks.Investors'),
        ),
    ]