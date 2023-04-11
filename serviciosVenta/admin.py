from django.contrib import admin
from serviciosVenta import models

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    list_display=("nombre", "precio")
    search_fields=("nombre",)
    list_filter=("precio",)

# class ClienteAdmin(admin.ModelAdmin):
#     list_display=("nombre", "dni", "localidad", "tipo_cliente")
#     search_fields=("nombre", "dni", "localidad", "tipo_cliente")
#     list_filter=("localidad", "tipo_cliente")

class AutoAdmin(admin.ModelAdmin):
    list_display=("patente", "marca", "modelo", "anio", "precio", "disponible")
    search_fields=("patente", "marca", "modelo", "anio", "precio", "disponible")
    list_filter=("marca", "anio", "disponible")

# class FacturaAdmin(admin.ModelAdmin):
#     list_display = ("id", "monto", "dni_cliente", "detalle")
#     search_fields = ("id", "fecha" , "monto", "dni_cliente", "detalle")
#     list_filter = ("fecha",)
#     date_hierarchy="fecha"

admin.site.register(models.Servicio, ServicioAdmin)
# admin.site.register(models.Cliente, ClienteAdmin)
admin.site.register(models.Auto, AutoAdmin)
# admin.site.register(models.Factura, FacturaAdmin)