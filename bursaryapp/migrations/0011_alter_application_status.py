# Generated by Django 4.0.4 on 2022-06-27 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bursaryapp', '0010_application_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.BooleanField(null=True),
        ),
    ]
