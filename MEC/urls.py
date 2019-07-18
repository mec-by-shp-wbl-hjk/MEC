from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.urls import include
from MECboard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',views.list, name='list'),
    path('join/', views.join, name='join'),
    path('login/', views.login_check, name='login'),
    
    url(r'^oauth/',include('social_django.urls', namespace ='social')),
    
    path('logout/',views.logout, name='logout'),
    path('write', views.write),
    path('insert', views.insert),
    path('download', views.download),
    path('detail', views.detail),
    path('update', views.update),
    path('delete', views.delete),
    path('reply_insert', views.reply_insert),
    path('update_page', views.update_page),
]