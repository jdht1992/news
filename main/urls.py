from django.contrib import admin
from django.urls import path
from .views import NewListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',NewListView.as_view(), name='new_list')
] 

