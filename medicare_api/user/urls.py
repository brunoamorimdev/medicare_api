from django.urls import path
import user.views as views

urlpatterns = [
    path(
        "<str:unique_id>/",
        views.UserRUDView.as_view(),
        name="user_read_update_destroy_api_view",
    ),
    path("", views.UserLCView.as_view(), name="user_list_create_api_view"),
]
