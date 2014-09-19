# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('group_ptr', models.OneToOneField(serialize=False, to='auth.Group', auto_created=True, primary_key=True, parent_link=True)),
                ('detail', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'permissions': (('view_company', 'Is member of Company'),),
                'ordering': ['name'],
                'verbose_name_plural': 'Companies',
            },
            bases=('auth.group',),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time', models.TimeField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(to='company.Company')),
            ],
            options={
                'permissions': (('view_company', 'Is member of Company'),),
            },
            bases=(models.Model,),
        ),
    ]
