from django.urls import path
from .views import GetBilling

urlpatterns = [
    path('billing/', GetBilling.as_view())
]