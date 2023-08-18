from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import User, Account, Card


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AccountSerializer(ModelSerializer):
    user = UserSerializer

    class Meta:
        model = Account
        fields = '__all__'


class CardSerializer(ModelSerializer):
    account = AccountSerializer

    class Meta:
        model = Card
        fields = '__all__'
