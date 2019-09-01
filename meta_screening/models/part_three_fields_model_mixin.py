from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from edc_constants.choices import YES_NO, YES_NO_NA
from edc_model.validators import hm_validator

from ..choices import OGTT_UNITS, SERUM_CREATININE_UNITS


class PartThreeFieldsModelMixin(models.Model):

    part_three_report_datetime = models.DateTimeField(
        verbose_name="Second stage report date and time",
        null=True,
        blank=False,
        help_text="Date and time of report.",
    )

    weight = models.DecimalField(
        null=True,
        blank=False,
        max_digits=8,
        decimal_places=4,
        validators=[MinValueValidator(15), MaxValueValidator(135)],
        help_text="in kgs",
    )

    height = models.IntegerField(
        null=True,
        blank=False,
        validators=[MinValueValidator(100), MaxValueValidator(230)],
        help_text="in centimeters",
    )

    fasted = models.CharField(
        verbose_name="Has the participant fasted?",
        max_length=15,
        choices=YES_NO,
        null=True,
        blank=False,
    )

    fasted_duration_str = models.CharField(
        verbose_name="How long have they fasted?",
        max_length=8,
        validators=[hm_validator],
        null=True,
        blank=True,
        help_text="format HH:MM",
    )

    fasted_duration_minutes = models.IntegerField(
        null=True, help_text="system calculated value"
    )

    urine_bhcg = models.CharField(
        verbose_name="Urine BHCG",
        max_length=15,
        choices=YES_NO_NA,
        null=True,
        blank=False,
        help_text="(Pregnancy test)",
    )

    hba1c = models.DecimalField(
        verbose_name="HbA1c",
        max_digits=8,
        decimal_places=4,
        null=True,
        blank=False,
        help_text="in %",
    )

    creatinine = models.DecimalField(
        verbose_name="Serum creatinine levels",
        max_digits=8,
        decimal_places=4,
        null=True,
        blank=False,
    )

    creatinine_units = models.CharField(
        verbose_name="Units (creatinine)",
        max_length=15,
        choices=SERUM_CREATININE_UNITS,
        null=True,
        blank=False,
    )

    # IFG
    fasting_glucose = models.DecimalField(
        verbose_name="Fasting glucose levels",
        max_digits=8,
        decimal_places=4,
        validators=[MinValueValidator(1), MaxValueValidator(50)],
        null=True,
        blank=False,
        help_text="mmol/L",
    )

    fasting_glucose_datetime = models.DateTimeField(
        verbose_name="Time fasting glucose level measured", null=True, blank=False
    )

    ogtt_performed_datetime = models.DateTimeField(
        verbose_name="Time oral glucose tolerance test was performed",
        null=True,
        blank=False,
        help_text="(glucose solution given)",
    )

    ogtt_two_hr = models.DecimalField(
        verbose_name="Blood glucose levels 2-hours after glucose solution given",
        max_digits=8,
        decimal_places=4,
        validators=[MinValueValidator(1), MaxValueValidator(300)],
        null=True,
        blank=False,
    )

    ogtt_two_hr_units = models.CharField(
        verbose_name="Units (Blood glucose)",
        max_length=15,
        choices=OGTT_UNITS,
        null=True,
        blank=False,
    )

    ogtt_two_hr_datetime = models.DateTimeField(
        verbose_name="Time blood glucose levels tested after glucose solution given",
        null=True,
        blank=False,
    )

    ogtt_two_hr_duration = models.CharField(
        verbose_name="Is the duration within range (110-130min)?",
        max_length=15,
        choices=YES_NO,
        null=True,
        blank=False,
        help_text="Duration will be calculated when you click SAVE.",
    )

    class Meta:
        abstract = True