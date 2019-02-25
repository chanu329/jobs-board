# Generated by Django 2.1.7 on 2019-02-25 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utime', models.IntegerField()),
                ('job_id', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('comments', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
