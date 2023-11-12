from django.urls import path, include
from core.views import HealthCheckView
import user.urls as urls

urlpatterns = [
    path("", HealthCheckView.as_view(), name="health_check_urls"),
    path("user/", include("user.urls"), name="user_urls"),
    path("professional/", include("professional.urls"), name="professional_urls"),
]
