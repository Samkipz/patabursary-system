# Generated by Django 4.0.4 on 2022-06-20 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='death_cert_father',
            field=models.FileField(blank=True, upload_to='pics', verbose_name='Death Certificate of Father'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='death_cert_mother',
            field=models.FileField(blank=True, upload_to='pics', verbose_name='Death Certificate of Mother'),
        ),
    ]
