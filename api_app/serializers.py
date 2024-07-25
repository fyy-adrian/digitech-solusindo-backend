from rest_framework import serializers
from .models import *


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class PortofolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portofolio
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class PartnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partnership
        fields = '__all__'

class CombinedSerializer(serializers.Serializer):
    heroes = HeroSerializer(many=True)
    prices = PriceSerializer(many=True)