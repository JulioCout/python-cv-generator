from django.contrib import admin
from django.urls import path
from cvGenerator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.accept, name='accept'),
    path('<int:id>/', views.resume, name='resume'),
    path('list/', views.list,name='list')
]
