# Generated by Django 3.0.4 on 2020-03-18 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpt2_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]