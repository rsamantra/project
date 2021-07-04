from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^create-item/$', CreateItemAPIView.as_view(),name="create-item"),
]