from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from . import views
from honeypot.views import fake_admin

urlpatterns = [
    path("admin/", fake_admin, name="honeypot-admin"),
    path("securelogin/", admin.site.urls),
    path("", views.home, name="home"),
    path("store/", include("store.urls")),
    path("cart/", include("carts.urls")),
    path("accounts/", include("accounts.urls")),
    path("orders/", include("orders.urls")),
]

# Serve uploaded media even when DEBUG=False
urlpatterns += [
    re_path(r"^media/(?P<path>.*)$", serve,
            {"document_root": settings.MEDIA_ROOT}),
]
