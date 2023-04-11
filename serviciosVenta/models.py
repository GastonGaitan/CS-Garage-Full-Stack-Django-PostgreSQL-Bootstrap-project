from django.db import models

# Create your models here.

class Servicio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000)
    precio = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.nombre}"
    
    
# class Cliente(models.Model):
#     dni = models.CharField(max_length=8, unique=True, primary_key=True)
#     nombre = models.CharField(max_length=80)
#     localidad = models.CharField(max_length=100)
#     tipo_cliente = models.CharField(max_length=80)

#     def __str__(self) -> str:
#         return f"{self.nombre} | {self.dni}"
    

class Auto(models.Model):
    patente = models.CharField(max_length=100, default=None, null=False, primary_key=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    kilometros = models.IntegerField()
    disponible = models.BooleanField()
    descripcion = models.CharField(max_length=1000)
    image=models.ImageField(upload_to='serviciosVenta/photos', default=None)
    # dni_anterior_duenio = models.ForeignKey(Cliente, default=None, on_delete=models.RESTRICT)
    precio = models.IntegerField(default=None)

    def __str__(self) -> str:
        return f"{self.marca} {self.modelo} | {self.anio}"

    class Meta:
        ordering = ['-disponible']

# class Factura(models.Model):
#     dni_cliente = models.CharField(max_length=7)
#     monto = models.IntegerField()
#     fecha = models.DateTimeField()
#     detalle = models.CharField(max_length=100, default=None)
#     descripcion_extra = models.CharField(max_length=1000, default=None)

    
    