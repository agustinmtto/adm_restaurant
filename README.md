# Sistema de Facturación para Restaurantes

Este proyecto es un sistema de facturación desarrollado en Python utilizando la biblioteca **Tkinter** para la creación de interfaces gráficas. El sistema permite calcular los costos de comidas, bebidas y postres, generar un recibo detallado y guardar los datos del recibo en un archivo.

## Características

- **Selección de productos:** Permite elegir entre una lista de comidas, bebidas y postres.
- **Cálculo automático:** Calcula el costo total de los productos seleccionados, incluyendo impuestos.
- **Recibo:** Genera un recibo detallado con la fecha y hora de la transacción.
- **Guardar recibo:** Permite guardar el recibo en un archivo de texto.
- **Interfaz intuitiva:** Diseñada con Tkinter para facilitar su uso.

## Requisitos

- Python 3.x
- Biblioteca estándar de Python (Tkinter)

## Instrucciones de uso

1. **Ejecutar el programa:** Abre el archivo Python en tu entorno de desarrollo o terminal y ejecútalo.
2. **Seleccionar productos:**
   - Marca las casillas de los productos que deseas comprar.
   - Introduce la cantidad deseada en los cuadros habilitados.
3. **Calcular el total:**
   - Haz clic en el botón "Total" para calcular el costo total, incluyendo impuestos.
4. **Generar recibo:**
   - Haz clic en "Recibo" para visualizar los detalles de la compra.
5. **Guardar recibo:**
   - Haz clic en "Guardar" para almacenar el recibo en un archivo de texto.
6. **Reiniciar el sistema:**
   - Haz clic en "Resetear" para limpiar los datos y comenzar una nueva transacción.

## Estructura del programa

- **Panel de productos:** Listas de comidas, bebidas y postres con sus respectivas casillas y campos de cantidad.
- **Panel de costos:** Muestra los costos desglosados de los productos, subtotal, impuestos y total.
- **Panel de recibo:** Área para visualizar y guardar el recibo generado.
- **Calculadora:** Incluye una calculadora básica integrada para realizar operaciones rápidas.

## Personalización

Puedes modificar las listas de productos y precios en las variables `lista_comidas`, `lista_bebidas`, `lista_postres` y sus respectivos precios en `precios_comida`, `precios_bebida` y `precios_postres`.

## Advertencia
* El script está siendo adaptado para funcionar correctamente en Windows, donde se ha detectado un problema de compatibilidad en el ajuste de la ventana.


## Autor

Agustin Maretto. Desarrollado como un ejemplo educativo de un sistema de facturación para restaurantes. 
