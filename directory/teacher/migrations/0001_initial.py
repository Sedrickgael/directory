# Generated by Django 3.2.7 on 2021-09-20 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('statut', models.BooleanField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subjects',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=254)),
                ('profile_picture', models.ImageField(default='default.png', upload_to='Teachers/Profile_Picture')),
                ('phone_number', models.CharField(max_length=50)),
                ('room_number', models.CharField(max_length=10)),
                ('statut', models.BooleanField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('subjects_taught', models.ManyToManyField(blank=True, to='teacher.Subject')),
            ],
            options={
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
            },
        ),
    ]
