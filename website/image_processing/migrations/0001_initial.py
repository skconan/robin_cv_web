# Generated by Django 2.1.3 on 2018-11-27 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('mask', models.BooleanField(default=False)),
            ],
        ),
    ]
