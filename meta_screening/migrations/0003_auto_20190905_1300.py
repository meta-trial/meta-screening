# Generated by Django 2.2.3 on 2019-09-05 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meta_screening', '0002_auto_20190905_1212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalscreeningpartone',
            name='ogtt_two_hr_duration',
        ),
        migrations.RemoveField(
            model_name='historicalscreeningpartthree',
            name='ogtt_two_hr_duration',
        ),
        migrations.RemoveField(
            model_name='historicalscreeningparttwo',
            name='ogtt_two_hr_duration',
        ),
        migrations.RemoveField(
            model_name='historicalsubjectscreening',
            name='ogtt_two_hr_duration',
        ),
        migrations.RemoveField(
            model_name='subjectscreening',
            name='ogtt_two_hr_duration',
        ),
    ]