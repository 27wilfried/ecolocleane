# Generated by Django 4.0.4 on 2023-10-13 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_devis'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvisUtilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etoiles', models.IntegerField()),
                ('commentaire', models.TextField()),
            ],
        ),
    ]