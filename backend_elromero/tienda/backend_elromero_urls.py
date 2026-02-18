from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from tienda import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tienda.urls')),
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)