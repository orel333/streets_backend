from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from contacts.views import ContactViewSet
from blog.views import BlogPostViewSet
from aboutus.views import (AboutUsViewSet, FederalTeamViewSet,
                                     RegionalTeamViewSet, PartnerTypeViewSet,
                                     PartnerViewSet, GalleryViewSet, MediaViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Your Project API",
        default_version='v1',
        description="API documentation for your project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourproject.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'v1/blog', BlogPostViewSet, basename='blog')
router.register(r'v1/contacts', ContactViewSet, basename='contacts')
router.register(r'v1/aboutus', AboutUsViewSet, basename='aboutus')
router.register(r'v1/federalteam', FederalTeamViewSet, basename='federalteam')
router.register(r'v1/regionalteam', RegionalTeamViewSet, basename='regionalteam')
router.register(r'v1/partnertype', PartnerTypeViewSet, basename='partnertype')
router.register(r'v1/partner', PartnerViewSet, basename='partner')
router.register(r'v1/gallery', GalleryViewSet, basename='gallery')
router.register(r'v1/media', MediaViewSet, basename='media')

urlpatterns = [
     path('admin/', admin.site.urls),
     path('', include(router.urls)),
     re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]