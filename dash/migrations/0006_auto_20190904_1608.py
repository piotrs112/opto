# Generated by Django 2.2.4 on 2019-09-04 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0005_auto_20190904_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='value',
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='surname',
            field=models.CharField(max_length=30, null=True),
        ),
    ]