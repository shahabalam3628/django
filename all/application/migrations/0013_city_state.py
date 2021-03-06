# Generated by Django 2.2.7 on 2020-03-28 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0012_author_book_publisher'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=30)),
                ('city_code', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=20)),
                ('state_code', models.CharField(max_length=4)),
                ('city', models.ManyToManyField(to='application.City')),
            ],
        ),
    ]
