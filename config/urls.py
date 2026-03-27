from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path

from apps.menu.views import FoodsListAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/foods/", FoodsListAPIView.as_view(), name="foods-list"),
] + debug_toolbar_urls()
