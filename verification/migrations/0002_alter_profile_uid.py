# Generated by Django 4.1.2 on 2022-11-11 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.CharField(default='<function uuid4 at 0x7f4b133fc9d0>', max_length=200),
        ),
    ]