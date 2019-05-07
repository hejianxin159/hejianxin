# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'verbose_name': '照片', 'verbose_name_plural': '照片'},
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(verbose_name='入侵人员照片', upload_to='images'),
        ),
    ]
