from django.utils.safestring import mark_safe


def get_part_one_fieldset(collapse=None):

    dct = {
        "description": "To be completed by the research nurse",
        "fields": (
            "report_datetime",
            "hospital_identifier",
            "initials",
            "gender",
            "age_in_years",
            "ethnicity",
            "hiv_pos",
            "art_six_months",
            "on_rx_stable",
            "lives_nearby",
            "staying_nearby",
            "pregnant",
            "preg_test_date",
            "consent_ability",
        ),
    }
    if collapse:
        dct.update(classes=("collapse",))
    return ("Part 1", dct)


def get_part_two_fieldset(collapse=None):
    dct = {
        "description": "To be completed by the study clinician",
        "fields": (
            "congestive_heart_failure",
            "liver_disease",
            "alcoholism",
            "acute_metabolic_acidosis",
            "renal_function_condition",
            "tissue_hypoxia_condition",
            "acute_condition",
            "metformin_sensitivity",
            "advised_to_fast",
            "appt_datetime",
        ),
    }
    if collapse:
        dct.update(classes=("collapse",))
    return ("Part 2", dct)


def get_part_three_fieldset(collapse=None):
    dct = {
        "description": "To be completed by the study clinician",
        "fields": (
            "weight",
            "height",
            "fasted",
            "fasted_duration_str",
            "urine_bhcg",
            "hba1c",
            "creatinine",
            "creatinine_units",
            "fasting_glucose",
            "fasting_glucose_datetime",
            "ogtt_performed_datetime",
            "ogtt_two_hr",
            "ogtt_two_hr_units",
            "ogtt_two_hr_datetime",
            "ogtt_two_hr_duration",
        ),
    }
    if collapse:
        dct.update(classes=("collapse",))
    return ("Part 3: Biomedical Indicators at Second Screening", dct)


special_exclusion_fieldset = (
    "Special Exclusion",
    {
        "description": mark_safe(
            "To be completed by the study clinician, if necessary."
            "<BR>A positive response, (e.g. YES), in this section <B>only</B> "
            "applies to criteria that is outside of the protocol "
            "inclusion and exclusion criteria above. "
        ),
        "fields": ("unsuitable_for_study", "reasons_unsuitable"),
    },
)

calculated_values_fieldset = (
    "Calculated values",
    {
        "classes": ("collapse",),
        "fields": (
            "calculated_bmi",
            "calculated_egfr",
            "converted_creatinine",
            "converted_ogtt_two_hr",
            "inclusion_a",
            "inclusion_b",
            "inclusion_c",
            "inclusion_d",
        ),
    },
)