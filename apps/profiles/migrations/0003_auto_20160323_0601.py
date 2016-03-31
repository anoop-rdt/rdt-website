# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('logo', models.FileField(upload_to=b'uploads/logos')),
                ('description', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='backend_technologies',
            field=models.ManyToManyField(related_name='backend_technologies', to='profiles.Technology'),
        ),
        migrations.AddField(
            model_name='client',
            name='frontend_technologies',
            field=models.ManyToManyField(related_name='frontend_technologies', to='profiles.Technology'),
        ),
    ]
