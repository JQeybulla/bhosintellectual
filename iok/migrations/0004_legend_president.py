# Generated by Django 3.0.6 on 2020-05-23 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iok', '0003_idare_heyeti'),
    ]

    operations = [
        migrations.CreateModel(
            name='Legend_president',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('name', models.TextField()),
            ],
        ),
    ]
