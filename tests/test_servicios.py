import pytest

from serviciosVenta.models import Servicio

@pytest.mark.django_db
def test_modelo_servicio():
    servicio = Servicio.objects.create(nombre="Lavado", descripcion="Limpiar el auto", precio=1000)
    servicio.save()
    servicios = Servicio.objects.all()
    assert len(servicios) > 0