from django.conf.urls import include, url
from django.views.generic.base import RedirectView

from rest_framework import routers
from rest_framework.authtoken import views

from . import viewsets


router = routers.DefaultRouter()
router.register(r'applications', viewsets.ApplicationViewSet)

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='api/v1/', permanent=False)),
    url(r'^api/v1/', include(router.urls)),
]
