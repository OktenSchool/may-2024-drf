"""
URL configuration for configs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="About Pizza",
        default_version='v1',
        description="Pizza Shop",
        contact=openapi.Contact(email="admin@gmail.com")
    ), public=True,
    permission_classes=[AllowAny],
)
urlpatterns = [
    path('api/pizzas', include('apps.pizza.urls')),
    path('api/pizza_shops', include('apps.pizza_shop.urls')),
    path('api/auth', include('apps.auth.urls')),
    path('api/users', include('apps.user.urls')),
    path('api/doc', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
