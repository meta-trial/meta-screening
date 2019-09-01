from edc_reportable import (
    MILLIGRAMS_PER_DECILITER,
    MILLIMOLES_PER_LITER,
    MICROMOLES_PER_LITER,
    MICROMOLES_PER_LITER_DISPLAY,
)
from edc_constants.constants import BLACK, OTHER, NOT_APPLICABLE, YES, NO


ETHNICITY = ((BLACK, "Black"), (OTHER, "Other"))

OGTT_UNITS = (
    (MILLIGRAMS_PER_DECILITER, MILLIGRAMS_PER_DECILITER),
    (MILLIMOLES_PER_LITER, MILLIMOLES_PER_LITER),
)

SERUM_CREATININE_UNITS = (
    (MILLIGRAMS_PER_DECILITER, MILLIGRAMS_PER_DECILITER),
    (MICROMOLES_PER_LITER, MICROMOLES_PER_LITER_DISPLAY),
)


YES_NO_NOT_ELIGIBLE = (
    (YES, YES),
    (NO, NO),
    (
        NOT_APPLICABLE,
        ("Not applicable, subject is not eligible based on the criteria above"),
    ),
)
