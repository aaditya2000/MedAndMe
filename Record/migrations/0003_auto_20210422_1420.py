# Generated by Django 3.1.6 on 2021-04-22 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Record', '0002_alter_record_ailment_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='recordfile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]