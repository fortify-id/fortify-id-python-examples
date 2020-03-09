"""democlient URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path(r'openid/openid/<op_name>', views.openid, name='openid_with_op_name'),
    re_path(r'openid/callback/login/?$', views.authz_cb, name='openid_login_cb'),
    path(r'openid/', include('djangooidc.urls')),
    path('app/', include('app.urls')),
    path('', RedirectView.as_view(url='/app'))
]

if getattr(settings,'ADMIN_ENABLED'):
    urlpatterns += [
        path('admin/', admin.site.urls),
    ]
