from apps.user.serializers import UserSerializer
from rest_framework import serializers
from .models import Cotacao, Wallet

class CotacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cotacao
        fields = '__all__'

class WalletSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Wallet
        fields = '__all__'