# Generated by Django 2.2.7 on 2020-03-31 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0013_city_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('publish', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['city_name']},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'ordering': ['state_name']},
        ),
        migrations.AlterField(
            model_name='city',
            name='city_name',
            field=models.CharField(help_text='Enter City Name', max_length=30),
        ),
    ]