# Generated by Django 4.2.3 on 2023-07-04 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webSBLS', '0011_delete_contacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrep', models.CharField(max_length=100)),
                ('correop', models.EmailField(max_length=254)),
                ('mensajep', models.TextField()),
            ],
        ),
    ]