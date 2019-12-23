from django.urls import path
from .views import browse_page

app_name = 'django_sftpbrowser'
urlpatterns = [
    path('', browse_page, name='sftp-index'),
    path('<path:input_path>', browse_page, name='sftp-resource'),
]
