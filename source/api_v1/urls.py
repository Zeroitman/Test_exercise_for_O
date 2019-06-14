from django.urls import include, path
from rest_framework import routers
from api_v1 import views

router = routers.SimpleRouter()
router.register(r'short', views.UserShortViewSet)
router.register(r'numbers', views.UserNumberViewSet)
router.register(r'user', views.UserViewSet)

app_name = 'api_v1'

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]