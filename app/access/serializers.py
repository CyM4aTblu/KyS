from rest_framework import serializers


class CheckAccessSerializer(serializers.Serializer):
    user = serializers.CharField(min_length=3, max_length=20, required=True)
    resource = serializers.CharField(min_length=3, required=True)


class AccessSerializer(serializers.Serializer):
    read = serializers.BooleanField(default=False)
    write = serializers.BooleanField(default=False)
    execute = serializers.BooleanField(default=False)


class ModifyAccessSerializer(CheckAccessSerializer, AccessSerializer):
    pass


class ForbiddenAccessSerializer(serializers.Serializer):
    forbidden = serializers.DictField(
        child=serializers.ListField(
            child=serializers.CharField()
        )
    )


class ValidationErrorSerializer(serializers.Serializer):
    errors = serializers.DictField(
        child=serializers.ListField(
            child=serializers.CharField()
        )
    )


class OperationSerializer(serializers.Serializer):
    id = serializers.CharField(required=True, min_length=36, max_length=36)
    done = serializers.BooleanField()
    result = serializers.DictField()


class GetOperationQuerySerializer(serializers.Serializer):
    id = serializers.UUIDField(required=True)

class ReplaceTextSerializer(serializers.Serializer):
    text = serializers.CharField(min_length=1, max_length=255, required=True)

class ReplaceTextByCountSerializer(ReplaceTextSerializer):
    count = serializers.IntegerField(min_value=1, required=True)

class HistoryEntrySerializer(serializers.Serializer):
    before = serializers.CharField(min_length=2, max_length=255, required=True)
    after = serializers.CharField(min_length=2, max_length=255, required=True)

class QueryHistorySerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True, min_value=0)
