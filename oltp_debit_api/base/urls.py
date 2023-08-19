from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoints),

    # User endpoints
    path('users/', views.UserList.as_view()),
    path('users/<str:pk>', views.UserDetail.as_view()),

    # Account endpoints
    path('accounts/', views.AccountList.as_view()),
    path('accounts/<str:pk>', views.AccountDetail.as_view()),

    # Card endpoints
    path('cards/', views.CardList.as_view()),
    path('cards/<str:pk>', views.CardDetail.as_view()),
]
