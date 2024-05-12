from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from blog.views import BlogPostViewSet

router = routers.DefaultRouter()
router.register(r'blog', BlogPostViewSet, basename='blog')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
