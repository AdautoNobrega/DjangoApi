from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from testapp import views

schema_view = get_swagger_view(title='TestApp API')

router = routers.DefaultRouter()
router.register(r'ocupacao', views.OcupacaoViewSet)
router.register(r'referencia', views.ReferenciaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    url('swagger/', schema_view)
]
