from uuid import UUID
from django.http import JsonResponse
import re
from django.shortcuts import render
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import AccessLogStatus
from .services.access_service import AccessService
from .services.log_service import LogService
from .serializers import (
    ModifyAccessSerializer,
    ValidationErrorSerializer,
    ReplaceTextSerializer, QueryHistorySerializer, HistoryEntrySerializer, ReplaceTextByCountSerializer
)

from .services.ops_service import OperationsService
from .services.replaceservices import ReplaceService


class ReplaceViewSet(ViewSet):
    @extend_schema(
        summary="Replace the letters 'ё' with 'е'",
        request=ReplaceTextSerializer,
        responses={
            status.HTTP_200_OK: ReplaceTextSerializer,
            status.HTTP_422_UNPROCESSABLE_ENTITY: ValidationErrorSerializer,
        },
        auth=False,
    )
    @action(detail=False, methods=["POST"])
    def process_text_e(self, request):
        in_text = ReplaceTextSerializer(data=request.data)
        if not in_text.is_valid():
            return Response(
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
                data=ValidationErrorSerializer({"errors": in_text.errors}).data,
            )
        out_text = ReplaceService.replace_e(in_text.data["text"])
        return Response(
            status=status.HTTP_200_OK,
            data=ReplaceTextSerializer({"text": out_text}).data
        )

    @extend_schema(
        summary="Replace the letters 'й' with 'и'",
        request=ReplaceTextSerializer,
        responses={
            status.HTTP_200_OK: ReplaceTextSerializer,
            status.HTTP_422_UNPROCESSABLE_ENTITY: ValidationErrorSerializer,
        },
        auth=False,
    )
    @action(detail=False, methods=["POST"])
    def process_text_i(self, request):
        in_text = ReplaceTextSerializer(data=request.data)
        if not in_text.is_valid():
            return Response(
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
                data=ValidationErrorSerializer({"errors": in_text.errors}).data,
            )
        out_text = ReplaceService.replace_i(in_text.data["text"])
        return Response(
            status=status.HTTP_200_OK,
            data=ReplaceTextSerializer({"text": out_text}).data
        )

    @extend_schema(
        summary="Replace the letters 'й' with 'и' by count",
        request=ReplaceTextByCountSerializer,
        responses={
            status.HTTP_200_OK: ReplaceTextSerializer,
            status.HTTP_422_UNPROCESSABLE_ENTITY: ValidationErrorSerializer,
        },
        auth=False,
    )
    @action(detail=False, methods=["PATCH"])
    def patch_text_i_by_count(self, request):
        in_text = ReplaceTextByCountSerializer(data=request.data)
        if not in_text.is_valid():
            return Response(
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
                data=ValidationErrorSerializer({"errors": in_text.errors}).data,
            )
        out_text = ReplaceService.replace_i_by_count(in_text.data["text"], in_text.data["count"])
        return Response(
            status=status.HTTP_200_OK,
            data=ReplaceTextSerializer({"text": out_text}).data
        )

    @extend_schema(
        summary="Replace the letters 'ё' with 'е' by count",
        request=ReplaceTextByCountSerializer,
        responses={
            status.HTTP_200_OK: ReplaceTextSerializer,
            status.HTTP_422_UNPROCESSABLE_ENTITY: ValidationErrorSerializer,
        },
        auth=False,
    )
    @action(detail=False, methods=["PATCH"])
    def patch_text_e_by_count(self, request):
        in_text = ReplaceTextByCountSerializer(data=request.data)
        if not in_text.is_valid():
            return Response(
                status=status.HTTP_422_UNPROCESSABLE_ENTITY,
                data=ValidationErrorSerializer({"errors": in_text.errors}).data,
            )
        out_text = ReplaceService.replace_e_by_count(in_text.data["text"], in_text.data["count"])
        return Response(
            status=status.HTTP_200_OK,
            data=ReplaceTextSerializer({"text": out_text}).data
        )