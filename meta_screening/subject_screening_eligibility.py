from edc_screening import if_yes, if_no, if_normal, GenderEvaluator

from .eligibility import Eligibility
from .reportables import age_evaluator


class EligibilityError(Exception):
    pass


class Eligibility:

    """Eligible if all criteria evaluate True.

    Any key in `additional_criteria` has value True if eligible.
    """

    gender_evaluator_cls = GenderEvaluator
    age_evaluator = age_evaluator

    def __init__(
        self,
        age=None,
        gender=None,
        **additional_criteria,
    ):

        self.criteria = dict(**additional_criteria)
        if len(self.criteria) == 0:
            raise EligibilityError("No criteria provided.")

        self.gender_evaluator = self.gender_evaluator_cls(
            gender=gender
        )
        self.criteria.update(age=self.age_evaluator.eligible(age))
        self.criteria.update(gender=self.gender_evaluator.eligible)

        # eligible if all criteria are True
        self.eligible = all([v for v in self.criteria.values()])
        if self.eligible:
            self.reasons_ineligible = None
        else:
            self.reasons_ineligible = {k: v for k,
                                       v in self.criteria.items() if not v}
            for k, v in self.criteria.items():
                if not v:
                    if k in self.custom_reasons_dict:
                        self.reasons_ineligible.update(
                            {k: self.custom_reasons_dict.get(k)}
                        )
                    elif k not in ["age", "gender"]:
                        self.reasons_ineligible.update({k: k})
            if not self.age_evaluator.eligible(age):
                self.reasons_ineligible.update(
                    age=self.age_evaluator.reasons_ineligible
                )
            if not self.gender_evaluator.eligible:
                self.reasons_ineligible.update(
                    gender=f"{' and '.join(self.gender_evaluator.reasons_ineligible)}."
                )

    def __str__(self):
        return self.eligible

    @property
    def custom_reasons_dict(self):
        """Returns a dictionary of custom reasons for named criteria.
        """
        custom_reasons_dict = dict(
            consent_ability="Not able or unwilling to give ICF.",
        )
        for k in custom_reasons_dict:
            if k in custom_reasons_dict and k not in self.criteria:
                raise EligibilityError(
                    f"Custom reasons refer to invalid named criteria, Got '{k}'. "
                    f"Expected one of {list(self.criteria)}. "
                    f"See {repr(self)}."
                )
        return custom_reasons_dict


class SubjectScreeningEligibility:

    eligibility_cls = Eligibility

    def __init__(self, model_obj=None, allow_none=None):
        eligibility_obj = self.eligibility_cls(
            allow_none=allow_none,
            age=model_obj.age_in_years,
            gender=model_obj.gender,
            consent_ability=model_obj.consent_ability,
            subject_screening=model_obj,
        )
        self.eligible = eligibility_obj.eligible
        self.reasons_ineligible = eligibility_obj.reasons_ineligible
