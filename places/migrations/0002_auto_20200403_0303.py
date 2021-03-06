# Generated by Django 3.0.4 on 2020-04-03 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='place',
            name='features',
            field=models.ManyToManyField(to='places.Feature'),
        ),
    ]
