# Generated by Django 3.0.6 on 2020-05-23 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iok', '0009_table_teampointtable'),
    ]

    operations = [
        migrations.CreateModel(
            name='legend_teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('team_name', models.TextField()),
                ('player_names', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Table',
        ),
    ]
