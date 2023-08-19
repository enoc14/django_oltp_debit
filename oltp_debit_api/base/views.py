from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from django.db.models import Q

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User, Account, Card

from .serializers import UserSerializer, AccountSerializer, CardSerializer


# Create your views here.
@api_view(['GET'])
def endpoints(request):
    data = ['/users', 'users/:id', '/accounts', 'accounts/:id', '/cards', 'cards/:id']
    return Response(data)


############################ USERS ############################
class UserList(APIView):
    @staticmethod
    def get(request):
        query = request.GET.get('query')
        if query is None:
            query = ''

        users = User.objects.filter(Q(name__icontains=query) | Q(city__icontains=query))
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    @staticmethod
    def get_object(pk):
        try:
            return User.objects.get(id=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def patch(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(instance=user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(data='The user has been deleted', status=status.HTTP_204_NO_CONTENT)


########################### ACCOUNTS ###########################
class AccountList(APIView):
    @staticmethod
    def get(request):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = AccountSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountDetail(APIView):
    @staticmethod
    def get_object(pk):
        try:
            return Account.objects.get(id=pk)
        except Account.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        account = self.get_object(pk)
        serializer = AccountSerializer(account)
        return Response(serializer.data)

    def patch(self, request, pk):
        account = self.get_object(pk)
        serializer = AccountSerializer(instance=account, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        account = self.get_object(pk)
        account.delete()
        return Response(data='The account has been deleted', status=status.HTTP_204_NO_CONTENT)


############################# CARDS #############################
class CardList(APIView):
    @staticmethod
    def get(request):
        query = request.GET.get('query')
        if query is None:
            query = ''

        cards = Card.objects.filter(Q(name__icontains=query))
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = CardSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CardDetail(APIView):
    @staticmethod
    def get_object(pk):
        try:
            return Card.objects.get(id=pk)
        except Card.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        card = self.get_object(pk)
        serializer = CardSerializer(card)
        return Response(serializer.data)

    def patch(self, request, pk):
        card = self.get_object(pk)
        serializer = CardSerializer(instance=card, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        card = self.get_object(pk)
        card.delete()
        return Response(data='The card has been deleted', status=status.HTTP_204_NO_CONTENT)
