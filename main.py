from fastapi import FastAPI
from typing import List
from data import compras_data, pasivos_data,ventas_data, gastos_data, cuentas_por_cobrar_data,cuentas_por_pagar_data,activos_data,capital_contable_data,transacciones_bancarias_data,impuestos_data, asientos_contables_data,estados_financieros_data
import uvicorn

app = FastAPI()


@app.get("/compras/getall", response_model=List[dict])
async def getAllCompras():
    return compras_data



@app.get("/ventas/getall", response_model=List[dict])
async def getAllVentas():
    return ventas_data


@app.get("/gastos/getall", response_model=List[dict])
async def getAllGastos():
    return gastos_data


@app.get("/cuentasporcobrar/getall", response_model=List[dict])
async def getAllCuentasPorCobrar():
    return cuentas_por_cobrar_data


@app.get("/cuentasporpagar/getall", response_model=List[dict])
async def getAllCuentasPorPagar():
    return cuentas_por_pagar_data



@app.get("/activos/getall", response_model=List[dict])
async def getAllActivos():
    return activos_data



@app.get("/pasivos/getall", response_model=List[dict])
async def getAllPasivos():
    return pasivos_data



@app.get("/capitalcontable/getall", response_model=List[dict])
async def getAllCapitalContable():
    return capital_contable_data


@app.get("/transaccionesbancarias/getall", response_model=List[dict])
async def getAllTransaccionesBancarias():
    return transacciones_bancarias_data



@app.get("/impuestos/getall", response_model=List[dict])
async def getAllImpuestos():
    return impuestos_data


@app.get("/asientoscontables/getall", response_model=List[dict])
async def getAllAsientosContables():
    return asientos_contables_data



@app.get("/estadosfinancieros/getall", response_model=List[dict])
async def getAllEstadosFinancieros():
    return estados_financieros_data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
