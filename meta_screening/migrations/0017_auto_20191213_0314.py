# Generated by Django 2.2.7 on 2019-12-13 00:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meta_screening", "0016_auto_20191119_2331"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalscreeningpartone",
            name="weight",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="in kgs",
                max_digits=8,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(15),
                    django.core.validators.MaxValueValidator(180),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningpartthree",
            name="weight",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="in kgs",
                max_digits=8,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(15),
                    django.core.validators.MaxValueValidator(180),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="historicalscreeningparttwo",
            name="weight",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="in kgs",
                max_digits=8,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(15),
                    django.core.validators.MaxValueValidator(180),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="historicalsubjectscreening",
            name="weight",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="in kgs",
                max_digits=8,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(15),
                    django.core.validators.MaxValueValidator(180),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="subjectscreening",
            name="weight",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                help_text="in kgs",
                max_digits=8,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(15),
                    django.core.validators.MaxValueValidator(180),
                ],
            ),
        ),
    ]
