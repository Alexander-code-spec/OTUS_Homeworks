# Generated by Django 3.2 on 2022-01-11 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('furniture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='furniture',
            name='code',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]