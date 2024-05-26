from fastapi import FastAPI
from typing import List
import data
import uvicorn
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.get("/compras/getall", response_model=List[dict])
async def getAllCompras():
    return data.compras_data



@app.get("/ventas/getall", response_model=List[dict])
async def getAllVentas():
    return data.ventas_data


@app.get("/gastos/getall", response_model=List[dict])
async def getAllGastos():
    return data.gastos_data


@app.get("/cuentasporcobrar/getall", response_model=List[dict])
async def getAllCuentasPorCobrar():
    return data.cuentas_por_cobrar_data


@app.get("/cuentasporpagar/getall", response_model=List[dict])
async def getAllCuentasPorPagar():
    return data.cuentas_por_pagar_data



@app.get("/activos/getall", response_model=List[dict])
async def getAllActivos():
    return data.activos_data



@app.get("/pasivos/getall", response_model=List[dict])
async def getAllPasivos():
    return data.pasivos_data



@app.get("/capitalcontable/getall", response_model=List[dict])
async def getAllCapitalContable():
    return data.capital_contable_data


@app.get("/transaccionesbancarias/getall", response_model=List[dict])
async def getAllTransaccionesBancarias():
    return data.transacciones_bancarias_data



@app.get("/impuestos/getall", response_model=List[dict])
async def getAllImpuestos():
    return data.impuestos_data


@app.get("/asientoscontables/getall", response_model=List[dict])
async def getAllAsientosContables():
    return data.asientos_contables_data



@app.get("/estadosfinancieros/getall", response_model=List[dict])
async def getAllEstadosFinancieros():
    return data.estados_financieros_data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
