# Generated by Django 3.1.2 on 2020-11-09 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure', models.CharField(max_length=80)),
                ('arrival', models.CharField(max_length=80)),
                ('price', models.IntegerField()),
                ('book_link', models.CharField(max_length=120)),
            ],
        ),
    ]
