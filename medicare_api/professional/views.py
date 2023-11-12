from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
)
from professional.serializers import ProfessionalSerializer, ProfessionSerializer
from professional.models import Profession


class ProfessionalLCRUDView(CreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = ProfessionalSerializer
    queryset = Profession.objects.all()
    lookup_field = "id"


class ProfessionLCView(ListCreateAPIView):
    serializer_class = ProfessionSerializer
    queryset = Profession.objects.all()
