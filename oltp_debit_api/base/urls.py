from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoints),

    # User endpoints
    path('users/', views.UserList.as_view()),

    # Account endpoints
    path('accounts/', views.AccountList.as_view()),

    # Card endpoints
    path('cards/', views.CardList.as_view()),
]
