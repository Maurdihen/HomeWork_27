"""
URL configuration for HomeWork_27 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from abs import views
from categories import views as categ

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.MainView.as_view()),
    path('abs/', views.AbsView.as_view()),
    path('cat/', categ.CategoriesView.as_view()),
    path('cat/<int:pk>', categ.CategoriesEntityView.as_view()),
    path('abs/<int:pk>', views.AdsEntityView.as_view()),
]
