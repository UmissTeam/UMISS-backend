"""umiss_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from body_sign import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'heartbeats', views.HeartBeatsViewSet)
router.register(r'galvanicresistance', views.GalvanicResistanceViewSet)
router.register(r'skintemperature', views.SkinTemperatureViewSet)
# router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [url(r'^', include(router.urls)), url(
    r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))]
