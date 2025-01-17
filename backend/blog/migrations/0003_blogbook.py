# Generated by Django 3.0.6 on 2020-12-10 17:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20201210_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('thumbnail', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('excerpt', models.CharField(max_length=150)),
                ('month', models.CharField(max_length=3)),
                ('day', models.CharField(max_length=2)),
                ('date_created', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.BlogPost')),
            ],
        ),
    ]
