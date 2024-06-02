from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from hydroponic_system_app.views import HydroponicSystemViewSet
from measurements_app.views import MeasurementsViewSet
from sensor_app.views import SensorViewSet

router = routers.SimpleRouter()
router.register(r'sensor', SensorViewSet)
router.register(r'measurements', MeasurementsViewSet)
router.register(r'hydroponic-system', HydroponicSystemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/app-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(router.urls)),
]
