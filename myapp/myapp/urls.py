from django.urls import path,include
from myapp import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',views.inicio),
    path('inicio',views.inicio),
    path('about', views.about),
    path('contacto', views.contacto),
    path("pacientes", views.pacientes, name="Paciente"),
    path("turnos", views.turnos, name="Turno"),
    path("doctores", views.doctores, name="Doctor"),
    #vistas basicas
    
    
    
   #vistas formularios
    
    
    
    
    path('pag404',views.pag404, name="pag404"),
    
    path('login', views.login_request, name='login'),
    path('register',views.register, name='registro'),
    path('logout',LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarPerfil', views.editarPerfil, name="editarPerfil"),
    #vistas de login/logout/register
    
    path ('formularioPaciente', views.formularioPaciente, name="FormularioPaciente"),
    path('buscarPas',views.buscarPas),
    path('editarPaciente/<paciente_dni>',views.editarPas, name="editarPaciente"),
    path('eliminarPaciente/<paciente_dni>/', views.eliminarPaciente, name="eliminarPaciente"),
    
    path ('formularioTurno', views.formularioTurno, name="FormularioTurno"),
    path ('buscarTur',views.buscarTur),
    path('editarTurno/<turno_dni>',views.editarTur, name="editarTurno"),
    path('eliminarTurno/<turno_dni>/', views.eliminarTurno, name="eliminarTurno"),
    
    path ('formularioDoctor', views.formularioDoctor, name="FormularioDoctor"),
    path ('buscarDoc',views.buscarDoc),
    path('editarDoctor/<doctor_dni>',views.editarDoc, name="editarDoctor"),
    path('eliminarDoctor/<doctor_dni>/', views.eliminarDoctor, name="eliminarDoctor"),

    path('pageAdmin',views.pageAdmin, name="pageAdmin"),
    path('crudDocAdm',views.crudDocAdm, name="crudDocAdm"),
    path('crudTurAdm',views.crudTurAdm, name="crudTurAdm"),
    path('crudPacAdm',views.crudPacAdm, name="crudPacAdm"),
    #vistas de crud de Admins
]