from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views
from groups.views import ListGroups

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ListGroups.as_view(), name='home'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('posts/', include('posts.urls', namespace='posts')),
    path('groups/', include('groups.urls', namespace='groups')),
    path('test/', views.TestPage.as_view(), name='test'),
    path('thanks/', views.ThanksPage.as_view(), name='thanks')
]
