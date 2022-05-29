from django.urls import path
from apps.autor import views

urlpatterns = [
    path('autor/inicio', views.ainicio, name= 'ainicio'),
    path('autor/create/', views.acreate, name = 'acreate'),
    path('autor/update/<int:id>', views.aupdate, name ='aupdate'),
    path('autor/delete/<int:id>', views.adelete, name = 'adelete'),
    path('libro/inicio', views.linicio, name= 'linicio'),
    path('libro/create/', views.lcreate, name = 'lcreate'),
    path('libro/update/<int:id>', views.lupdate, name ='lupdate'),
    path('libro/delete/<int:id>', views.ldelete, name = 'ldelete'),
    path('autorlibro/inicio', views.alinicio, name= 'alinicio'),
    path('autorlibro/create/', views.alcreate, name = 'alcreate'),
    path('autorlibro/update/<int:id>', views.alupdate, name ='alupdate'),
    path('autorlibro/delete/<int:id>', views.aldelete, name = 'aldelete'),
]