# Generated by Django 2.0.1 on 2018-01-21 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(default='default', unique=True)),
                ('content', models.TextField()),
                ('category', models.CharField(choices=[('BACKEND', 'Backend'), ('FRONTEND', 'Frontend'), ('DEPLOYMENT', 'Deployment')], default='BACKEND', max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('premium', models.BooleanField(default=False)),
            ],
        ),
    ]
