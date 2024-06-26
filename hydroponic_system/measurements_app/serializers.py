from rest_framework import serializers

from measurements_app.models import Measurements


class MeasurementsSerializer(serializers.ModelSerializer):
    """
    Measurements Serializer converting complex data types into Python data types
    """
    sensor = serializers.StringRelatedField()
    owner = serializers.PrimaryKeyRelatedField(read_only=True)
    hydroponic_system = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Measurements
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'owner')
