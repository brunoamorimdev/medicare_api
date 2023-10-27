from django.db import connections
from django.http import JsonResponse
from rest_framework.views import APIView


class HealthCheckView(APIView):
    def get(self, request):
        health_status = self.check_health()
        return JsonResponse({"status": health_status})

    def check_health(self):
        # Check database connectivity
        database_errors = []
        for alias in connections:
            connection = connections[alias]
            try:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT 1;")
            except Exception as e:
                database_errors.append(f"Database error ({alias}): {str(e)}")

        if database_errors:
            return "unhealthy"

        # You can add more health checks here
        # For example, check external services, file system access, etc.

        return "healthy"
