# Generated by Django 3.2 on 2021-04-16 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Record', '0001_initial'),
        ('Medicine', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicine',
            name='record',
        ),
        migrations.AddField(
            model_name='medicine',
            name='record',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Record.record'),
        ),
    ]
