from django.urls import include, path
import api.urls as api_patterns

urlpatterns = [
    path("api/", include((api_patterns, "api"))),
]
