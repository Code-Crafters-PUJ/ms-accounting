
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all_compras():
    response = client.get("/compras/getall")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_get_all_ventas():
    response = client.get("/ventas/getall")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_get_all_gastos():
    response = client.get("/gastos/getall")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_get_all_cuentas_por_cobrar():
    response = client.get("/cuentasporcobrar/getall")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_get_all_activos():
    response = client.get("/activos/getall")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_get_all_pasivos():
    response = client.get("/pasivos/getall")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_get_all_transacciones_bancarias():
    response = client.get("/transaccionesbancarias/getall")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_get_all_impuestos():
    response = client.get("/impuestos/getall")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_get_all_asientos_contables():
    response = client.get("/asientoscontables/getall")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

def test_get_all_estados_financieros():
    response = client.get("/estadosfinancieros/getall")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0

if __name__ == "__main__":
    pytest.main()
