# Generated by Django 4.2.1 on 2023-05-22 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webSBLS', '0003_alter_trabajo_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='foto',
            field=models.ImageField(null=True, upload_to='fotos'),
        ),
    ]
