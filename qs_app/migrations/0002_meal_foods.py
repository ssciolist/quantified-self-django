# Generated by Django 2.0.7 on 2018-07-06 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qs_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='foods',
            field=models.ManyToManyField(to='qs_app.Food'),
        ),
    ]
