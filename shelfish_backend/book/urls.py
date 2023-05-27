from django.urls import path
from .views import TodoAPIView, OrdersView

urlpatterns = [
    path("orders", OrdersView.as_view()),
    path("books", TodoAPIView.as_view()),
    path("books/<str:pk>", TodoAPIView.as_view()),  # to capture our ids
]
