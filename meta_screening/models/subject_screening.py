from django.db import models
from edc_constants.choices import YES_NO, PREG_YES_NO_NA
from edc_model.models import BaseUuidModel
from edc_screening.model_mixins import ScreeningModelMixin

from ..subject_screening_eligibility import SubjectScreeningEligibility


class SubjectScreening(ScreeningModelMixin, BaseUuidModel):

    eligibility_cls = SubjectScreeningEligibility

    hospital_identifier = models.CharField(max_length=25, unique=True)

    hiv_pos = models.CharField(
        verbose_name="Is the patient HIV positive",
        max_length=5,
        choices=YES_NO,
    )

    art_six_months = models.CharField(
        verbose_name=(
            "Has the patient been on anti-retroviral therapy for at least 6 months"),
        max_length=10, choices=YES_NO
    )

    on_rx_stable = models.CharField(
        verbose_name=(
            "Is the patient considered to be stable on treatment "
            "(in regular attendance for care)"),
        max_length=10, choices=YES_NO
    )

    lives_nearby = models.CharField(
        verbose_name=(
            "Is the patient living within the catchment population of the facility"),
        max_length=10, choices=YES_NO
    )

    staying_nearby = models.CharField(
        verbose_name=(
            "Is the patient planning to remain in the catchment area "
            "for at least 6 months"),
        max_length=10, choices=YES_NO
    )

    pregnancy = models.CharField(
        verbose_name="Is the patient pregnant?", max_length=15, choices=PREG_YES_NO_NA
    )

    preg_test_date = models.DateTimeField(
        verbose_name="Pregnancy test (Urine or serum βhCG) date", blank=True, null=True
    )

    congestive_heart_failure = models.CharField(
        verbose_name=(
            "Does the patient have congestive heart failure "
            "requiring pharmacologic therapy"),
        max_length=15, choices=YES_NO
    )

    liver_disease = models.CharField(
        verbose_name=(
            "Is there clinical evidence of liver disease"),
        max_length=15, choices=YES_NO,
        help_text=(
            "Evidence of chronic liver disease: Jaundice, pruritus, "
            "hepatomegaly, ascites, spider naevi and flapping tremors.")
    )

    alcoholism = models.CharField(
        verbose_name=(
            "Does the patient have any evidence of alcoholism or "
            "acute alcohol intoxication"),
        max_length=15, choices=YES_NO,
        help_text=(
            "Evidence of alcoholism or acute alcohol intoxication: "
            "flushing, amnesia, mental confusion, nausea or vomiting, "
            "slurred speech, dehydration, dry skin and brittle hair.")
    )

    acute_metabolic_acidosis = models.CharField(
        verbose_name=(
            "Does the patient have any signs or symptoms of acute metabolic acidosis "
            "(lactic acidosis and/or diabetic ketoacidosis)"),
        max_length=15, choices=YES_NO
    )
    renal_function_condition = models.CharField(
        verbose_name=(
            "Does the patient have any acute condition which can alter renal "
            "function including: dehydration, severe infection or shock"),
        max_length=15, choices=YES_NO
    )

    tissue_hypoxia_condition = models.CharField(
        verbose_name=(
            "Does the patient have any acute condition which can cause tissue "
            "hypoxia"),
        max_length=15, choices=YES_NO,
        help_text=("Including: decompensated heart failure, respiratory failure, "
                   "recent myocardial infarction or shock")
    )

    acute_condition = models.CharField(
        verbose_name=(
            "Does the patient have any acute condition requiring "
            "immediate hospital care/admission"),
        max_length=15, choices=YES_NO
    )

    metformin_sensitivity = models.CharField(
        verbose_name=(
            "Does the patient have any known hypersensitivity to metformin "
            "or any excipients associated with its preparation"),
        max_length=15, choices=YES_NO,
        help_text=(
            "For example: Magnesium stearate, sodium "
            "carboxymethylcellulose, hypromellose")
    )
