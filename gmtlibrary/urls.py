from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='gmtlibrary-home'),
    # path('', views.courses, name='gmtlibrary-courses'),
    path('upload/', views.upload, name = 'gmtlibrary-upload'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)