# Generated by Django 2.0.7 on 2019-03-10 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookorder',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
