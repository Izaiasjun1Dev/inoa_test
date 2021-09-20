from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.cotacoes.views import WalletViewSet

# Documentation: https://www.django-rest-framework.org/api-guide/routers/
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# Schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Wallet api",
        default_version='v1',
        description="",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="solucaprogramer@gmail.com"),
        license=openapi.License(name="BSD License"),
    public=True,
    permission_classes=[permissions.AllowAny],
    )
)

router = routers.DefaultRouter()
router.register('cotacao', WalletViewSet, basename='cotacoes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('doc-api/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc')
]


from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apps.cotacoes.views import WalletViewSet

# Documentation: https://www.django-rest-framework.org/api-guide/routers/
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# Schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Schoool API",
        default_version='v1',
        description="documentations descriptivebles",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="solucaoprogramer@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)



router = routers.DefaultRouter()
router.register('cotacao', WalletViewSet, basename='cotacoes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('doc-api/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc')
]

