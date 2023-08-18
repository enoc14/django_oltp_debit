from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User, Account, Card

from .serializers import UserSerializer, AccountSerializer, CardSerializer


# Create your views here.
@api_view(['GET'])
def endpoints(request):
    data = ['/path']
    return Response(data)


############################ USERS ############################
class UserList(APIView):
    @staticmethod
    def get(request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


########################### ACCOUNTS ###########################
class AccountList(APIView):
    @staticmethod
    def get(request):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)


############################# CARDS #############################
class CardList(APIView):
    @staticmethod
    def get(request):
        cards = Card.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)
