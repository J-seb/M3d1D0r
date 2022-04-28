# M3d1D0r

Pasos para la instalación.

1. Clic en code y copiar enlace para clonar repo por protocolo **HTTPS / SSH** o descarga directa como **.zip**.
2. Si se descargó como .zip descomprimirlo en carpeta.
3. Instalar virtualenv como dependencia global de **Python**
  > `pip install virtualenv`
4. Crear entorno virtual dentro de la ruta del proyecto
  > `python -m virtualenv venv`
5. Activar entorno virtual a partir de acá se debe trabajar con el entorno virtual activado.
  - (Windows - Verificar si existen permisos de políticas de ejecución)
  > `.\venv\Scripts\activate`
  - (Linux)
  > `source ./venv/bin/activate`
6. Instalar dependencias
  > `pip install -r requirements.txt`
7. Iniciar app
  > `python ./Prueba.py`
