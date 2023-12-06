# Generated by Django 4.2.7 on 2023-12-02 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('temoins', '0002_parti_politique_regroupement_politiuqe_and_more'),
        ('candidats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidats',
            name='centre_vote',
            field=models.ManyToManyField(to='temoins.centre_vote'),
        ),
        migrations.AddField(
            model_name='candidats',
            name='regroupement_politiuqe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='temoins.regroupement_politiuqe'),
        ),
        migrations.AddField(
            model_name='candidats',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reclamation',
            name='temoin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='temoins.temoins'),
        ),
        migrations.AddField(
            model_name='sollicite_temoin',
            name='temoin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='temoins.temoins'),
        ),
        migrations.AddField(
            model_name='sollicite_temoin',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
