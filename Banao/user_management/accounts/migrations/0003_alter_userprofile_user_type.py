# Generated by Django 5.0.2 on 2024-08-11 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_profile_user_userprofile_delete_customuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('admin', 'Admin'), ('doctor', 'Doctor'), ('patient', 'Patient')], max_length=10),
        ),
    ]
