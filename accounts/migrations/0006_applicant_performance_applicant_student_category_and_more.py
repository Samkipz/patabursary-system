# Generated by Django 4.0.4 on 2022-06-26 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_applicant_id_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='performance',
            field=models.FileField(blank=True, upload_to='pics', verbose_name='Latest transript'),
        ),
        migrations.AddField(
            model_name='applicant',
            name='student_category',
            field=models.CharField(choices=[('GSSP', 'GSSP'), ('PSSP Degree', 'PSSP Degree'), ('PSSP Diploma', 'PSSP Diploma')], default='GSSP', max_length=15),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='maritial_status',
            field=models.CharField(choices=[('Married', 'Married'), ('Single', 'Single')], max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
    ]
