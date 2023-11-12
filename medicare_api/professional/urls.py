from django.urls import path
import professional.views as views

urlpatterns = [
    path(
        "user/<slug:id>/",
        views.ProfessionalLCRUDView.as_view(),
        name="professional_create_api_view",
    ),
    path(
        "", views.ProfessionalLCRUDView.as_view(), name="professional_create_api_view"
    ),
    path(
        "profession/",
        views.ProfessionLCView.as_view(),
        name="profession_create_api_view",
    ),
]
