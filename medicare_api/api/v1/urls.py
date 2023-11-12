from django.urls.conf import include, path
import authentication.views as auth_views
import user.views as user_views
import admin.views as admin_views

auth_patterns = [path("", auth_views.AuthAPIView.as_view(), name="auth_token")]

user_patterns = [
    path(
        "permissions/",
        user_views.UserPermissionsAPI.as_view(),
        name="users_permissions_create_api_view",
    )
]

admin_patterns = [
    path(
        "users/permissions/content-types/",
        admin_views.AdminPermissionsContentTypesListAPIView.as_view(),
        name="admin_permissions_content_types_list_api_view",
    ),
    path(
        "users/permissions/",
        admin_views.AdminUsersPermissionsCreateAPIView.as_view(),
        name="admin_users_permissions_create_api_view",
    ),
]

urlpatterns = [
    path("users/", include((user_patterns, "users"))),
    path("auth/", include((auth_patterns, "auth"))),
    path("admin/", include((admin_patterns, "admin"))),
]
