from django.urls import path

from .views import check_in

urlpatterns = (
    path('', check_in),
)
