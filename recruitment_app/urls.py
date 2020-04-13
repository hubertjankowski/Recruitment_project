from django.conf.urls import url
from django.db import router
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from recruitment_app import views
from  recruitment_app.views import url_detail


router = DefaultRouter()
router.register(r'Users', views.UserViewSet)
router.register(r'Add_URL', views.AddURLViewSet)
router.register(r'View_details', views.ShortURLViewSet, basename='Details')


urlpatterns = [
    path('', include(router.urls)),
    url(r'^(?P<shorturl>[!0-9A-Za-z]{1,9})/$', url_detail, name='shorturl'),
]