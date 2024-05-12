from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from contacts.views import ContactViewSet

router = routers.DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contacts')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]