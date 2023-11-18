from django.db import models
from Cliente.models import Cliente  

class Auto(models.Model):
    patente = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    numero_de_ruedas = models.IntegerField()
    propietario = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='autos', default=1)

    
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.patente})"
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    fecha_de_nacimiento = models.DateField()
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    ordering = ['id']

    def __str__(self):
        return f"{self.nombre} ({self.email})"
