from django.urls import path
from .views import TodoAPIView

urlpatterns = [
        path('books', TodoAPIView.as_view()),
        path('books/<str:pk>', TodoAPIView.as_view()) # to capture our ids
]