# Generated by Django 4.1.2 on 2022-11-07 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0005_doctemplates_date_create_doctemplates_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='doctemplaterequisites',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='doctemplaterequisites',
            name='requisite',
            field=models.CharField(max_length=150, unique=True, verbose_name='Реквизит'),
        ),
    ]