# Generated by Django 4.0.4 on 2022-05-28 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Familiares', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='familia',
            name='parentesco',
            field=models.CharField(default='madre', max_length=50),
            preserve_default=False,
        ),
    ]
