# Generated by Django 2.0.7 on 2019-03-04 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_auto_20190304_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.IntegerField(db_column='author_age', null=True),
        ),
    ]
