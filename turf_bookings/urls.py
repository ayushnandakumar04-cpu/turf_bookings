"""
URL configuration for turf_bookings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from turf_management.views import TurfListCreateView,TurfRetrieveUpdateDeleteView,AdminRegister
from turf_Register.views import TurfRegisterListCreate,TurfRetrieveUpdateDelete
urlpatterns = [
    path('admin/', admin.site.urls),

    path('admin-register/',AdminRegister.as_view()),
    path('turff/',TurfListCreateView.as_view()),
    path("turff/<int:pk>/",TurfRetrieveUpdateDeleteView.as_view()),

    # turf team register booking rough
    path("register/",TurfRegisterListCreate.as_view()),
    path("register/<int:pk>/",TurfRetrieveUpdateDelete.as_view()),

      # booking_v2 route

    path('turf/',include('booking_v2.urls')),

]
