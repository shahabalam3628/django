# Generated by Django 2.2.7 on 2020-03-27 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_auto_20200326_1444'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('useremail', models.EmailField(max_length=29)),
                ('userpass', models.CharField(max_length=20)),
            ],
        ),
    ]
