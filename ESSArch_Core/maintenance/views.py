import os

from django.utils import timezone

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import exceptions, filters, status, viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response

from rest_framework_extensions.mixins import NestedViewSetMixin

from ESSArch_Core.configuration.models import Path
from ESSArch_Core.maintenance.filters import AppraisalJobFilter, AppraisalRuleFilter
from ESSArch_Core.maintenance.models import AppraisalJob, AppraisalRule
from ESSArch_Core.maintenance.serializers import AppraisalRuleSerializer, AppraisalJobSerializer
from ESSArch_Core.util import generate_file_response


class AppraisalRuleViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = AppraisalRule.objects.all()
    serializer_class = AppraisalRuleSerializer
    filter_class = AppraisalRuleFilter
    filter_backends = (
        filters.OrderingFilter, DjangoFilterBackend, filters.SearchFilter,
    )
    search_fields = ('name', 'specification',)


class AppraisalJobViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = AppraisalJob.objects.all()
    serializer_class = AppraisalJobSerializer
    filter_class = AppraisalJobFilter
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)

    @detail_route(methods=['get'])
    def report(self, request, pk=None):
        path = Path.objects.get(entity='appraisal_reports').value
        path = os.path.join(path, pk + '.pdf')

        with open(path) as pdf:
            return generate_file_response(pdf, 'application/pdf')

    @detail_route(methods=['post'])
    def run(self, request, pk=None):
        job = self.get_object()
        job.start_date = timezone.now()
        job.save()
        job.run()
        return Response(status=status.HTTP_202_ACCEPTED)