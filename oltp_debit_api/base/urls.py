from django.urls import path
from . import views

urlpatterns = [
    path('available-endpoints', views.endpoints),

    # User endpoints
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),

    # Account endpoints
    path('accounts/', views.AccountList.as_view()),
    path('accounts/<int:pk>', views.AccountDetail.as_view()),

    # Card endpoints
    path('cards/', views.CardList.as_view()),
    path('cards/<int:pk>', views.CardDetail.as_view()),
]
