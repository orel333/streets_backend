from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from contacts.views import ContactViewSet
from blog.views import BlogPostViewSet
from events.views import EventViewSet

router = routers.DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contacts')
router.register(r'blog', BlogPostViewSet, basename='blog')
router.register(r'events', EventViewSet, basename='events')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]