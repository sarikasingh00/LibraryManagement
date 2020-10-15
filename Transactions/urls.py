from django.contrib import admin
from django.urls import path, include
from Transactions import views as transaction_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('issue/<int:id>/', transaction_views.issue_books,name='issue-books'),
    # path('return/<int:id>/', transaction_views.return_books,name='return-books'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)