# Generated by Django 4.1.7 on 2023-04-12 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_user_is_customer_remove_user_is_employee_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmpID', models.IntegerField(max_length=25)),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('college', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=40)),
                ('is_phD', models.BooleanField()),
            ],
        ),
    ]
