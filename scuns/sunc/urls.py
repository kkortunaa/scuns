from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static 
from django.conf import settings
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('sunc/', views.sunc, name='sunc'),
]