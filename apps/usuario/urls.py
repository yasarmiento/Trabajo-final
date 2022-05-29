from django.urls import path
from apps.usuario import views

urlpatterns = [
    path('', views.uinicio, name= 'uinicio'),
    path('usuario/create/', views.ucreate, name = 'ucreate'),
    path('usuario/update/<int:id>', views.uupdate, name ='uupdate'),
    path('usuario/delete/<int:id>', views.udelete, name = 'udelete'),
    path('ejemplares', views.einicio, name= 'einicio'),
    path('ejemplares/create/', views.ecreate, name = 'ecreate'),
    path('ejemplares/update/<int:id>', views.eupdate, name ='eupdate'),
    path('ejemplares/delete/<int:id>', views.edelete, name = 'edelete'),
    path('prestar', views.pinicio, name= 'pinicio'),
    path('prestar/create/', views.pcreate, name = 'pcreate'),
    path('prestar/update/<int:id>', views.pupdate, name ='pupdate'),
    path('prestar/delete/<int:id>', views.pdelete, name ='pdelete'),
]