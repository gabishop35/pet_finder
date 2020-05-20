"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.urls import include, path
from pet_finder import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="home"),
    path('pet/add/', views.add_pet, name='add-pet'),
    path('pet/<int:pk>/edit/', views.edit_pet, name='edit-pet'),
    path('pet/<int:pk>/delete/', views.delete_pet, name='delete-pet'),
    path('profile/', views.profile_page, name='profile-page'),
    path('information/', views.info, name='info'),
    path('found/', views.found_pets, name='found-pets'),
    path('found/post/', views.post_found_pet, name='post-found-pet'),
    path('lost/', views.lost_pets, name='lost-pets'),
    path('accounts/', include('registration.backends.simple.urls')),


]

    # + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
