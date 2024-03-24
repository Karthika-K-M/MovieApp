from django.conf import settings

from . import views
from django.urls import path
from django.conf.urls.static import static

app_name = 'travelapp'
urlpatterns = [
    path('', views.demo, name='demo'),
    path('add/', views.add_mobile, name='add_mobile'),
    path('mobile/<int:mobile_id>/', views.details, name='details'),
    path('edit_mobile/<int:id>/',views.edit_mobile,name='edit_mobile'),
    path('delete/<int:id>/',views.delete,name='delete')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
