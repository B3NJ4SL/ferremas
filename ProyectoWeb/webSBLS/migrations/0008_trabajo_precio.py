# Generated by Django 4.2.3 on 2023-07-03 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webSBLS', '0007_trabajo_comentario_trabajo_publicado_trabajo_usuario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabajo',
            name='precio',
            field=models.IntegerField(default=100000),
        ),
    ]