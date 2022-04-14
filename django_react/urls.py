
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, GroupViewSet
from core.views import ListViewSet, ItemViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'List', ListViewSet)
router.register(r'item', ItemViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(router.urls)),
]