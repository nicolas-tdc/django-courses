# Generated by Django 3.2.8 on 2021-10-29 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='choices',
        ),
        migrations.AddField(
            model_name='question',
            name='choices',
            field=models.ManyToManyField(to='polls.Choice'),
        ),
    ]
