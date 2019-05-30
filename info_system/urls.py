from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('^login/', auth_views.LoginView.as_view()),
    url(r'^admin/', admin.site.urls,),
    url(r'^api/v1/catalog/', include('catalog.api_urls')),
    url(r'^', include('catalog.urls')), ]
