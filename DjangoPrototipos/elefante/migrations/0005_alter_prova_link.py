# Generated by Django 4.1 on 2022-10-13 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elefante', '0004_prova_link_alter_paper_correto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prova',
            name='link',
            field=models.CharField(default='dRwP6y9v11JdpMX8', max_length=20, unique=True),
        ),
    ]
