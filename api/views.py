from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters, pagination
from .models import Control
from .serializers import ControlSerializers
from rest_framework.response import Response
from django.http import FileResponse, HttpResponse
from rest_framework import viewsets, renderers
from rest_framework.decorators import action
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
import csv


# Pagination sets.
class PageSet(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = "size"
    max_page_size = 10
    page_query_param = "page"


# Control views.
class ControlViewSet(viewsets.ModelViewSet):
    queryset = Control.objects.all().order_by('pk')
    serializer_class = ControlSerializers
    pagination_class = PageSet

    # Overwrite the put request logic.
    def update(self, request, pk=None):
        control = self.get_object()
        for k, v in request.data.items():
            setattr(control, k, v)
            control.save()
        serializer = ControlSerializers(control)

        return Response(serializer.data)

    # Overwrite the get request logic.
    def retrieve(self, request, pk=None):
        queryset = Control.objects.all()
        control = get_object_or_404(queryset, pk=pk)
        serializer = ControlSerializers(control)

        return Response(serializer.data)

    # Upload a csv file and save the records into the db.
    @action(detail=False, methods=['post'])
    def upload(self, request, pk=None):
        csv_file = request.FILES["file"]
        file_data = csv_file.read().decode("utf-8")

        # Get rid of \r from the original file.
        file_data = file_data.replace("\r", "")
        lines = file_data.split("\n")

        # Leave out the first field name row.
        for line in lines[1:]:
            if not line:
                continue
            fields = line.split(",")
            control = Control(name=fields[0], type=fields[1], maximum_rabi_rate=fields[2], polar_angle=fields[3])
            control.save()

        return Response()

    # Download all the records into a csv file.
    @action(detail=False, methods=['get'])
    def download(self, request, pk=None):
        queryset = Control.objects.all()
        serializer = ControlSerializers(queryset, many=True)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="export.csv"'

        # Write to the response.
        writer = csv.writer(response)
        writer.writerow(ControlSerializers().Meta.fields)
        for row in serializer.data:
            writer.writerow(list(row.values()))

        return response


serializer_class = ControlSerializers
