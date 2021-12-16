# Generated by Django 3.2.10 on 2021-12-15 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=255, null=True)),
                ('lname', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
