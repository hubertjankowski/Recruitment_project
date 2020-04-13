from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('recruitment_app.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
