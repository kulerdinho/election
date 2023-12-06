# Generated by Django 4.2.7 on 2023-12-02 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('temoins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parti_politique',
            name='regroupement_politiuqe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='temoins.regroupement_politiuqe'),
        ),
        migrations.AddField(
            model_name='temoins',
            name='centre_vote',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='temoins.centre_vote'),
        ),
        migrations.AddField(
            model_name='temoins',
            name='regroupement_politiuqe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='temoins.regroupement_politiuqe'),
        ),
        migrations.AddField(
            model_name='temoins',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
