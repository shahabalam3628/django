# Generated by Django 2.2.7 on 2020-03-25 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_auto_20200325_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='stu_address',
            field=models.TextField(default=None, max_length=555),
        ),
        migrations.AddField(
            model_name='student',
            name='stu_gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=20),
        ),
        migrations.AddField(
            model_name='student',
            name='stu_mobile',
            field=models.CharField(default=None, max_length=11),
        ),
        migrations.AddField(
            model_name='student',
            name='stu_pincode',
            field=models.CharField(default=None, max_length=6),
        ),
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='father_name',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='stu_name',
            field=models.CharField(default=None, max_length=255),
        ),
    ]