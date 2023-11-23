from .views import OrderList, OrderDetail, RegisterView, LoginView, UserView, LogoutView
from django.urls import path

urlpatterns = [
    path("api/orders", OrderList.as_view(), name="orders"),
    path("api/orders/<int:pk>", OrderDetail.as_view(), name="order"),
    path('register', RegisterView.as_view(), name="register"),
    path('login', LoginView.as_view(), name="login"),
    path('user', UserView.as_view(), name="user"),
    path('logout', LogoutView.as_view(), name="logout"),
]