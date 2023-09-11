from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api', views.PersonViewSet)

urlpatterns = [
   # path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls))
]