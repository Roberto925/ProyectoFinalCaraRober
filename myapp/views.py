from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import HttpResponse
from .models import Doctor,Paciente,Turno,Avatar
from .forms import FormularioDoctor,FormularioPaciente,FormularioTurno,UserRegisterForm,UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.hashers import make_password

def login_request(request):
    if request.method=="POST":
        form= AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            usuario= form.cleaned_data.get('username')
            contras= form.cleaned_data.get('password')

            user= authenticate(username=usuario,password=contras)
            if user is not None:
                login(request,user)
                return render(request, "inicio.html", {"mensaje":f'Bienvenido {usuario}'})
            else:
                return render(request, "inicio.html", {"mensaje":f'Datos Incorrectos'})
        else:
            return render(request, "inicio.html",{"mensaje":"Error, Formulario Erroneo"})
    form=AuthenticationForm()
    return render(request,"login.html",{"form":form})

def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            
            return render(request, 'inicio.html',{'mensaje':"Usuario Creado con exito"})
    else:
        #form = UserCreationForm()
        form= UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    print(avatares[0].imagen.url)
    return render(request, 'inicio.html', {'url':avatares[0].imagen.url})



def about (request):
    avatares = Avatar.objects.filter(user=request.user.id)
    print(avatares[0].imagen.url)
    
    return render(request, 'about.html', {'url':avatares[0].imagen.url})

def pag404 (request):
    avatares = Avatar.objects.filter(user=request.user.id)
    print(avatares[0].imagen.url)
    return render(request, 'pag404.html', {'url':avatares[0].imagen.url})
@login_required





#Inicio Doctores
@user_passes_test(lambda u: u.groups.filter(name='Medico').exists())
def doctores(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    print(avatares[0].imagen.url)
    return render(request, 'doctores.html', {'url':avatares[0].imagen.url})

def formularioDoctor(request):
    if request.method=='POST':
        miFormulario=FormularioDoctor(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            doctor= Doctor(usuario=informacion['usuario'],nombre=informacion['nombre'],apellido=informacion['apellido'],dni= informacion['dni'],area=informacion['area'])
            doctor.save()
            return render(request,'inicio.html')
        else:
            miFormulario=FormularioTurno()       
    return render(request, "formularioDoctor.html")

def buscarDoc(request):   
    usuario = request.GET.get('usuario', '')
    doctor = Doctor.objects.filter(usuario__icontains=usuario)
    if doctor:
        context = {'doctor': doctor}
        return render(request, 'resultadoDoc.html', context)
    else:
        mensaje = "No se encontraron resultados para '{}'. Intente de nuevo.".format(usuario)
        context = {'mensaje': mensaje}
        return render(request, 'no_resultados.html', context)

def editarDoc(request, doctor_dni):
    doctor = Doctor.objects.get(dni=doctor_dni)
    if request.method == 'POST':
        miFormulario = FormularioDoctor(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            doctor.usuario= informacion['usuario']
            doctor.nombre = informacion['nombre']
            doctor.apellido = informacion['apellido']
            doctor.dni = informacion['dni']
            doctor.area = informacion['area']
            doctor.save()
            return render(request, "inicio.html")    
    else:
        miFormulario = FormularioTurno(initial={'usuario': doctor.usuario,'nombre': doctor.nombre, 'apellido': doctor.apellido,
                                                'dni': doctor.dni,'area': doctor.area})

        return render(request, 'editarDoctor.html',{"miFormulario":miFormulario, "doctor_dni":doctor_dni})
    
def eliminarDoctor(request, doctor_dni):
    doctor = Doctor.objects.get(dni=doctor_dni)
    doctor.delete()
    # vuelvo al menú
    doctor = Doctor.objects.all()  # trae todos los profesores
    contexto = {"doctor": doctor}
    return render(request, "resultadoDoc.html", contexto)



#Inicio Turno
def turnos(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    print(avatares[0].imagen.url)
    return render(request, 'turnos.html', {'url':avatares[0].imagen.url})

def formularioTurno(request):
    if request.method=='POST':
        miFormulario=FormularioTurno(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            turno= Turno(usuario=informacion['usuario'],paciente=informacion['paciente'],fecha=informacion['fecha'],dni= informacion['dni'],especial=informacion['especial'])
            turno.save()
            return render(request,'inicio.html')
        else:
            miFormulario=FormularioTurno()     
    return render(request, "formularioTurno.html",)

def buscarTur(request):   
    if request.GET['usuario']:
        usuario=request.GET['usuario']
        turno= Turno.objects.filter(usuario__icontains=usuario)
        context={'turno':turno}
        return render(request,'resultadoTur.html',context)
    else:
        respuesta= "No se encontro datos"
    return HttpResponse(respuesta)

def editarTur(request, turno_dni):
    turno = Turno.objects.get(dni=turno_dni)
    if request.method == 'POST':
        miFormulario = FormularioTurno(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            turno.usuario = informacion['usuario']
            turno.paciente = informacion['paciente']
            turno.fecha = informacion['fecha']
            turno.dni = informacion['dni']
            turno.especial = informacion['especial']
            turno.save()
            return render(request, "inicio.html")    
    else:
        miFormulario = FormularioTurno(initial={'usuario': turno.usuario, 'paciente': turno.paciente,
                                                   'fecha': turno.fecha, 'dni': turno.dni,
                                                   'especial': turno.especial})

        return render(request, 'editarTurno.html',{"miFormulario":miFormulario, "turno_dni":turno_dni})
    
def eliminarTurno(request, turno_dni):
    turno = Turno.objects.get(dni=turno_dni)
    turno.delete()
    # vuelvo al menú
    turno = Turno.objects.all()  # trae todos los profesores
    contexto = {"turno": turno}
    return render(request, "resultadoTur.html", contexto)



#Inicio Paciente
def pacientes(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    print(avatares[0].imagen.url)
    return render(request, 'pacientes.html', {'url':avatares[0].imagen.url})

def formularioPaciente(request):
    if request.method=='POST':
        miFormulario=FormularioPaciente(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            paciente= Paciente(usuario=informacion['usuario'],nombre=informacion['nombre'],apellido=informacion['apellido'],dni=informacion['dni'],obraSocial=informacion['obraSocial'])
            paciente.save()
            return render(request,'inicio.html')
        else:
            miFormulario=FormularioTurno()
    return render(request, "formularioPaciente.html")


def buscarPas(request):
    if request.GET['usuario']:
        usuario=request.GET['usuario']
        pacientes= Paciente.objects.filter(usuario__icontains=usuario)
        context={'pacientes':pacientes}
        return render(request,'resultado.html',context)
    else:
        respuesta= "No se encontro datos"
    return HttpResponse(respuesta)

def editarPas(request, paciente_dni):
    paciente = Paciente.objects.get(dni=paciente_dni)
    if request.method == 'POST':
        miFormulario = FormularioPaciente(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            paciente.usuario = informacion['usuario']
            paciente.nombre = informacion['nombre']
            paciente.apellido = informacion['apellido']
            paciente.dni = informacion['dni']
            paciente.obraSocial = informacion['obraSocial']
            paciente.save()
            return render(request, "inicio.html")
    else:
        miFormulario = FormularioPaciente(initial={'usuario': paciente.usuario, 'nombre': paciente.nombre,
                                                   'apellido': paciente.apellido, 'dni': paciente.dni,
                                                   'obraSocial': paciente.obraSocial})

        return render(request, 'editarPaciente.html',{"miFormulario":miFormulario, "paciente_dni":paciente_dni})  

def eliminarPaciente(request, paciente_dni):
    paciente = Paciente.objects.get(dni=paciente_dni)
    paciente.delete()
    # vuelvo al menú
    paciente = Paciente.objects.all()  # trae todos los profesores
    contexto = {"paciente": paciente}
    return render(request, "resultado.html", contexto)

@user_passes_test(lambda u: u.is_superuser)
def pageAdmin(request):
    return render(request, 'pageAdmin.html')
def crudTurdAdm(request):
    return render(request, 'crudTurAdm.html')

def crudPacAdm(request):
    return render(request, 'crudPacAdm.html')

def crudDocAdm(request):
    return render(request, 'crudDocAdm.html')

def contacto(request):
    return render(request, 'contacto.html')

def crudPacAdm(request):

      pacientes = Paciente.objects.all() #trae todos los profesores

      contexto= {"pacientes":pacientes} 

      return render(request, "crudPacAdm.html",contexto)

def crudDocAdm(request):

      doctores = Doctor.objects.all() #trae todos los profesores

      contexto= {"doctores":doctores} 

      return render(request, "crudDocAdm.html",contexto)

def crudTurAdm(request):

      turno = Turno.objects.all() #trae todos los profesores

      contexto= {"turno":turno} 

      return render(request, "crudTurAdm.html",contexto)

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data


            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            if informacion['password1'] == informacion['password2']:
                usuario.password = make_password(informacion['password1'])
                usuario.save()
            else:
                return render(request, 'inicio.html', {'mensaje':'Contrasena incorrecta'})


            return render(request, 'inicio.html')
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})


    return render(request, "editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})
