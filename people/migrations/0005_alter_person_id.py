# Generated by Django 4.2.5 on 2023-09-11 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_alter_person_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
