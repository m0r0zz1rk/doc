# Generated by Django 4.1.2 on 2022-11-11 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0009_alter_doctemplates_date_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctemplates',
            name='name',
            field=models.TextField(default='Шаблон', max_length=1500, verbose_name='Наименование шаблона'),
        ),
    ]