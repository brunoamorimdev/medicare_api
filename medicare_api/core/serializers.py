import rest_framework.serializers as serializers


class BasePaginationFilterSerializer(serializers.Serializer):
    page = serializers.IntegerField(required=False, min_value=1)
    page_size = serializers.IntegerField(required=False, min_value=1)
    pagination = serializers.CharField(required=False, max_length=10, default="")
