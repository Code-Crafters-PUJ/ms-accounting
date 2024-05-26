# ms-accounting

## Requisitos de Instalación
Antes de ejecutar la aplicación, asegúrate de tener instaladas las dependencias.
Puedes instalarlos usando pip y el archivo `requirements.txt` proporcionado:
   ```bash
   pip install -r requirements.txt
```

## Ejecucion
Abre una terminal o un símbolo del sistema en el directorio donde se encuentra tu proyecto.
Utiliza el siguiente comando para iniciar el servicio en el puerto 8080:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8080
```

## Ejecucion de pruebas unitarias
Para ejecutar las pruebas unitarias, nos podemos limitar a correr el siguiente comando:
   ```bash
   pytest
```
De esta manera, se ejecutará de manera automática el archivo test_main.py que contiene toda la lógica de las pruebas.