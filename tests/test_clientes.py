import pytest

from serviciosVenta.models import Cliente

@pytest.mark.django_db
def test_modelo_auto():
    cliente = Cliente.objects.create(
        dni = "41134345",
        nombre = "Gaston Gaitan",
        localidad = "Zarate",
        tipo_cliente = "Comprador",
    )
    cliente.save()
    clientes = Cliente.objects.all()
    assert len(clientes) > 0