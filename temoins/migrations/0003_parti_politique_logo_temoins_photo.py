# Generated by Django 4.2.7 on 2023-12-02 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temoins', '0002_parti_politique_regroupement_politiuqe_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='parti_politique',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='parti_politique/logo/'),
        ),
        migrations.AddField(
            model_name='temoins',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='temoins/photos/'),
        ),
    ]
