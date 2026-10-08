from django.urls import path
from booking_v2.views import SignUpRegisterView
from booking_v2.views import TurfBookingListCreateView

urlpatterns = [

    path('signup/',SignUpRegisterView.as_view()),

    path('booking/',TurfBookingListCreateView.as_view()),
]