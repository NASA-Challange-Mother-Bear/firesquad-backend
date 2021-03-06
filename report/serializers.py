from rest_framework_gis.serializers import GeoFeatureModelSerializer

from report.models import Report


class ReportSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Report
        fields = ('photo', 'timestamp', 'status', 'type', 'user', 'alert', 'id')
        geo_field = 'geolocation'
