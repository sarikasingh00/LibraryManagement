from django.contrib import admin
from django.urls import path, include
# from lib import views as lib_views
# from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views as fine_views

urlpatterns = [
    path('view/<int:id>/', fine_views.check_fines,name='view-fines'),
    path('pay/<int:id>/', fine_views.pay_fine,name='pay-fine'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)