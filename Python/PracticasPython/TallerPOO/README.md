# Gestión de Ventas de Entradas
Este proyecto de Python proporciona una aplicación de gestión para la venta de entradas de eventos deportivos, con las siguientes funcionalidades principales:
- **Registro de Clientes:** Permite a los clientes ingresar su nombre, número de identificación (DNI) y edad.
- **Selección de Eventos:** Los clientes pueden seleccionar entre diferentes partidos deportivos disponibles.
- **Selección de Asientos:** Visualización y selección de asientos disponibles para cada evento.
- **Selección de Tipo de Entrada:** Opciones para elegir entre entrada General o VIP, con cálculo automático del precio final.
- **Descuento Especial:** Aplicación de descuento del 50% para clientes cuyo DNI sea un "número vampiro".
- **Registro de Compra:** Confirmación y registro de la compra del boleto seleccionado, almacenando la información en un archivo de texto.

## Requisitos
- Python 3.x
- Bibliotecas estándar de Python: pathlib, re
- Archivos y módulos personalizados: utils, models

## Instalación
1. Clona o descarga este repositorio en tu máquina local.
```bash
git clone https://github.com/tu_usuario/gestion-ventas-entradas.git
```
2. Asegúrate de tener Python 3.x instalado.
3. Instala las dependencias necesarias:
```bash
pip install -r requirements.txt
```

## Uso
1. Ejecuta el programa principal:
```bash
python main.py
```
2. Sigue las instrucciones en consola para ingresar los datos del cliente, seleccionar un evento, elegir un tipo de entrada y un asiento disponible.
3. Confirma la compra cuando se te solicite.

## Estructura del Proyecto
- main.py: Punto de entrada principal del programa.
- utils/: Módulos y funciones auxiliares para el manejo de datos y filtros.
- models/: Definición de modelos de datos como Ticket.

## Contribución
Si deseas contribuir a este proyecto, por favor sigue estos pasos:
1. Haz un fork del repositorio y clónalo en tu máquina local.
2. Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
3. Realiza tus cambios y pruebas.
4. Confirma los cambios (git commit -m 'Añadir nueva funcionalidad').
5. Sube los cambios (git push origin feature/nueva-funcionalidad).
6. Crea un pull request detallando tus cambios.

## Créditos
Este proyecto fue desarrollado como parte de un curso de Algoritmos y Programación (BPTSP05).

## Licencia
Distribuido bajo la licencia MIT. Ver LICENSE para más información.