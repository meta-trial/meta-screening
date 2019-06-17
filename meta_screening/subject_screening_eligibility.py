from edc_screening import if_yes, if_no, if_normal

from .eligibility import Eligibility
from .gender_evaluator import GenderEvaluator
from .reportables import age_evaluator


class EligibilityError(Exception):
    pass


class Eligibility:

    """Eligible if all criteria evaluate True.

    Any key in `additional_criteria` has value True if eligible.
    """

    gender_evaluator_cls = GenderEvaluator
    # early_withdrawal_evaluator_cls = EarlyWithdrawalEvaluator
    age_evaluator = age_evaluator

    def __init__(
        self,
        age=None,
        gender=None,
        pregnant=None,
        breast_feeding=None,
        alt=None,
        neutrophil=None,
        platelets=None,
        allow_none=None,
        subject_screening=None,
        **additional_criteria,
    ):

        self.criteria = dict(**additional_criteria)
        if len(self.criteria) == 0:
            raise EligibilityError("No criteria provided.")

        self.gender_evaluator = self.gender_evaluator_cls(
            gender=gender, pregnant=pregnant, breast_feeding=breast_feeding
        )
#         self.early_withdrawal_evaluator = self.early_withdrawal_evaluator_cls(
#             alt=alt,
#             neutrophil=neutrophil,
#             platelets=platelets,
#             allow_none=allow_none,
#             subject_screening=subject_screening,
#         )
        self.criteria.update(age=self.age_evaluator.eligible(age))
        self.criteria.update(gender=self.gender_evaluator.eligible)
        self.criteria.update(
            early_withdrawal=self.early_withdrawal_evaluator.eligible)

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
                    elif k not in ["age", "gender", "early_withdrawal"]:
                        self.reasons_ineligible.update({k: k})
            if not self.age_evaluator.eligible(age):
                self.reasons_ineligible.update(
                    age=self.age_evaluator.reasons_ineligible
                )
            if not self.gender_evaluator.eligible:
                self.reasons_ineligible.update(
                    gender=f"{' and '.join(self.gender_evaluator.reasons_ineligible)}."
                )
            if not self.early_withdrawal_evaluator.eligible:
                self.reasons_ineligible.update(
                    {**self.early_withdrawal_evaluator.reasons_ineligible}
                )

    def __str__(self):
        return self.eligible

    @property
    def custom_reasons_dict(self):
        """Returns a dictionary of custom reasons for named criteria.
        """
        custom_reasons_dict = dict(
            no_drug_reaction="Previous adverse drug reaction to the study medication.",
            no_concomitant_meds="Patient on contraindicated medication.",
            meningitis_dx="Previous Hx of Cryptococcal Meningitis.",
            no_amphotericin="> 0.7mg/kg of Amphotericin B.",
            no_fluconazole="> 48hrs of Fluconazole.",
            will_hiv_test="HIV unknown or unwilling to test.",
            consent_ability="Not able or unwilling to give ICF.",
            not_suitable="Patient unsuitable for study.",
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
            alt=model_obj.alt,
            neutrophil=model_obj.neutrophil,
            platelets=model_obj.platelets,
            will_hiv_test=if_yes(model_obj.will_hiv_test),
            consent_ability=if_yes(model_obj.consent_ability),
            meningitis_dx=if_yes(model_obj.meningitis_dx),
            pregnant=if_yes(model_obj.pregnancy),
            breast_feeding=if_yes(model_obj.breast_feeding),
            no_drug_reaction=if_no(model_obj.previous_drug_reaction),
            no_concomitant_meds=if_no(model_obj.contraindicated_meds),
            no_amphotericin=if_no(model_obj.received_amphotericin),
            no_fluconazole=if_no(model_obj.received_fluconazole),
            not_suitable=if_no(model_obj.unsuitable_for_study),
            subject_screening=model_obj,
        )
        self.eligible = eligibility_obj.eligible
        self.reasons_ineligible = eligibility_obj.reasons_ineligible
