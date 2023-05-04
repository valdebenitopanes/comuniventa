
from products.views import ProductListView
from django.contrib import admin
from django.urls import include, path

from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', ProductListView.as_view(),name='index'),
    path('usuarios/salir', views.logout,name='logout'),
    path('login', views.login,name='login'),
    path('usuarios/registro', views.register,name='register'),
    path('admin/', admin.site.urls),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('products/', include('products.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)