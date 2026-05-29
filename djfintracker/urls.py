
from django.contrib import admin
from django.urls import path , include
from django.contrib.auth import urls as auth_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('finance.urls')),
    path('accounts/', include(auth_urls)),
]