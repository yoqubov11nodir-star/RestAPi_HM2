from django.urls import path
from .views import SmartphoneListAPIView

urlpatterns = [
    path('phones/', SmartphoneListAPIView.as_view()),
]