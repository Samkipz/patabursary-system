# Generated by Django 4.0.4 on 2022-07-06 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_applicant_performance_applicant_student_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
