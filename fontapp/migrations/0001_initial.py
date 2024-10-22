# Generated by Django 2.2.7 on 2019-12-01 00:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarShare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate', models.CharField(max_length=30)),
                ('start', models.CharField(max_length=90)),
                ('end', models.CharField(max_length=90)),
                ('date', models.CharField(max_length=90)),
                ('phone', models.IntegerField()),
                ('seat', models.IntegerField()),
                ('number', models.IntegerField()),
                ('mark', models.TextField()),
                ('type', models.IntegerField(default=1)),
                ('state', models.IntegerField(default=1)),
                ('createtime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日期')),
            ],
        ),
        migrations.CreateModel(
            name='ThirdParty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField()),
                ('content', models.CharField(max_length=120)),
                ('type', models.IntegerField(default=1)),
                ('state', models.IntegerField(default=1)),
                ('createtime', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日期')),
            ],
        ),
    ]
