# Generated by Django 4.2.7 on 2023-12-02 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temoins', '0003_parti_politique_logo_temoins_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centre_vote',
            name='code_centre',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
