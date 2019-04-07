from rest_framework import serializers
from ahck.models import Packet, Cargo, ServiceClass, Flight, SystemUser, ActOfShortage, Mock
import json


class DescriptionJson(serializers.Field):
    def to_internal_value(self, data):
        return {"description_in_json": data}
        
    def to_representation(self, value):
        return json.loads(value.description_in_json)


class PacketSerializer(serializers.ModelSerializer):
    description_in_json = DescriptionJson(source='*')
    class Meta:
        model = Packet
        fields = '__all__'


class CargoSerializer(serializers.ModelSerializer):
    packets = PacketSerializer(many=True, read_only=True)
    class Meta:
        model = Cargo
        fields = '__all__'


class ServiceClassSerializer(serializers.ModelSerializer):
    cargos = CargoSerializer(many=True, read_only=True)

    class Meta:
        model = ServiceClass
        fields = '__all__'


class FlightSerializer(serializers.ModelSerializer):
    servise_classes = ServiceClassSerializer(many=True, read_only=True)

    class Meta:
        model = Flight
        fields = '__all__'


class SystemUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemUser
        fields = '__all__'


class ActOfShortageSerializer(serializers.ModelSerializer):
    flight = FlightSerializer(many=True, read_only=True)
    description_in_json = DescriptionJson(source='*')
    class Meta:
        model = ActOfShortage
        fields = '__all__'


class MockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mock
        fields = '__all__'
