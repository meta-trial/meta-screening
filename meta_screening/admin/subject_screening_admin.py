from django.contrib import admin
from edc_model_admin import SimpleHistoryAdmin
from edc_model_admin.dashboard import ModelAdminSubjectDashboardMixin

from ..admin_site import meta_screening_admin
from ..forms import SubjectScreeningForm
from ..models import SubjectScreening


instructions = (
    "Patients must meet ALL of the inclusion criteria and NONE of the "
    "exclusion criteria in order to proceed to the final screening stage")


@admin.register(SubjectScreening, site=meta_screening_admin)
class SubjectScreeningAdmin(ModelAdminSubjectDashboardMixin, SimpleHistoryAdmin):

    form = SubjectScreeningForm

    post_url_on_delete_name = "screening_dashboard_url"
    subject_listboard_url_name = "screening_listboard_url"

    fieldsets = (
        (
            "Part 1: Initial Screening",
            {
                "fields": (
                    "report_datetime",
                    "hospital_identifier",
                    "gender",
                    "age_in_years",
                    "hiv_pos",
                    "art_six_months",
                    "on_rx_stable",
                    "lives_nearby",
                    "staying_nearby",
                    "pregnancy",
                    "preg_test_date",
                    "congestive_heart_failure",
                    "liver_disease",
                    "alcoholism",
                    "acute_metabolic_acidosis",
                    "renal_function_condition",
                    "tissue_hypoxia_condition",
                    "acute_condition",
                    "metformin_sensitivity",
                )
            },
        ),
        #         ("Part 2: Screening Results", {
        #             "fields": (
        #                 "alt", "neutrophil", "platelets"
        #             )
        #         }
        #         ),
        #         ("Part 3: Final Screening", {
        #             "fields": (
        #                 "alt", "neutrophil", "platelets"
        #             )
        #         }
        #         ),
    )

    radio_fields = {
        "gender": admin.VERTICAL,
        "hiv_pos": admin.VERTICAL,
        "art_six_months": admin.VERTICAL,
        "on_rx_stable": admin.VERTICAL,
        "lives_nearby": admin.VERTICAL,
        "staying_nearby": admin.VERTICAL,
        "pregnancy": admin.VERTICAL,
        "congestive_heart_failure": admin.VERTICAL,
        "liver_disease": admin.VERTICAL,
        "alcoholism": admin.VERTICAL,
        "acute_metabolic_acidosis": admin.VERTICAL,
        "renal_function_condition": admin.VERTICAL,
        "tissue_hypoxia_condition": admin.VERTICAL,
        "acute_condition": admin.VERTICAL,
        "metformin_sensitivity": admin.VERTICAL,
    }
