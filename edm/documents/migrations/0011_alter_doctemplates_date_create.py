# Generated by Django 4.1.2 on 2022-11-11 06:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0010_alter_doctemplates_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctemplates',
            name='date_create',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата создания шаблона'),
        ),
    ]