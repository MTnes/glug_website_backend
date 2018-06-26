# Generated by Django 2.0.6 on 2018-06-19 19:27

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180616_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=64, unique=True)),
                ('content', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
