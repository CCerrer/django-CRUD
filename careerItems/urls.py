from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'items', views.ItemViewSet, basename='items')
app_name = 'careerItems'

urlpatterns = [
    path('', include(router.urls)),
]
