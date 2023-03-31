from django.db import models
from django.contrib.auth.models import User

class Avatar(models.Model):
   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
 
    def __str__(self):
        return f"{self.user} - {self.imagen}"


class Paciente(models.Model):
    id=models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=30, default="doctorcito")
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    dni=models.CharField(max_length=30, default="00000000")
    obraSocial= models.CharField(max_length=30)
    def __str__(self):
        return f"id: {self.id}- usuario: {self.usuario}-nombre: {self.nombre}-apellido: {self.apellido}-dni:{self.dni}- obrasocial: {self.obraSocial}"
    

class Doctor(models.Model):
    id=models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=30,default="doctorcito")
    nombre=models.CharField(max_length=30, default="doctorcito")
    apellido= models.CharField(max_length=30)
    dni=models.CharField(max_length=30, default="00000000")
    area= models.CharField(max_length=30)
    def __str__(self):
        return f"id{self.id}- usuario: {self.usuario}- nombre: {self.nombre}- apellido: {self.apellido}- dni: {self.dni}- Area: {self.area}"

class Turno(models.Model):
    id=models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=30)
    paciente= models.CharField(max_length=30)
    fecha= models.CharField(max_length=30,default="dd/mm/aa")
    dni=models.CharField(max_length=30, default="00000000")
    especial= models.CharField(max_length=30)

    def __str__(self):
        return f"id: {self.id}- usuario: {self.usuario}- paciente: {self.paciente}- fecha: {self.fecha}- DNI: {self.dni}- especialidad: {self.especial}"

# Create your models here.
