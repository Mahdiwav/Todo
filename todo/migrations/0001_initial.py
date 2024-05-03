# Generated by Django 5.0.4 on 2024-04-09 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('priority', models.IntegerField(default=1)),
                ('is_done', models.BooleanField()),
            ],
            options={
                'db_table': 'todos',
            },
        ),
    ]