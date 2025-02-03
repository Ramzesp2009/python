from django.urls import path

from api.views import StudentAPIView


urlpatterns = [
    path('students/', StudentAPIView.as_view(), name='students'),
]
