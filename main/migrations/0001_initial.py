# Generated by Django 4.0.4 on 2022-07-06 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published_date', models.DateTimeField()),
                ('titles', models.TextField()),
                ('ids', models.TextField()),
                ('thumbnails', models.TextField()),
            ],
        ),
    ]