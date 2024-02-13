# PlaygroundFinalProject-Dalton
Entrega Final Curso Python Flex

## Nombre

- Nombre y apellido: Karina Dalton

- Link de LinkedIn: https://www.linkedin.com/in/karina-gabriela-dalton/

## Resumen del proyecto

- Desarrollo de una página web, en este caso de una tienda de articulos de decoración, donde se puede dar de alta, editar, consultar y eliminar artículos, categorias, transacciones de ventas y clientes.

## Pasos para ejecutar el proyecto

- Link de GitHub: https://github.com/karidalton/PlaygroundFinalProject-Dalton.git

- Dependencias utilizadas: Django 5.0.1

- Cómo ejecutar la aplicación web en el servidor local:

1) En una carpeta vacía abrir la terminal y ejecutar 'git clone https://github.com/karidalton/TuPrimeraPagina-Dalton'
2) Abrir el proyecto en VSC
3) En la terminal activar el entorno virtual ingresando en la terminal '.\.venv\Scripts\activate'
4) Para ejecutar el proyecto ejecutar en la terminal 'python manage.py runserver' y luego ingresar a la URL http://127.0.0.1:8000


## Lo realizado:
1) 3 apps: core, cliente y catalogo
- la app 'core' es la app principal, donde se encuentra el diseño base del HTML, así como el indice, la barra de navegación, footer, el contacto y sobre nosotros.
- la app 'cliente' contiene los modelos y vistas correspondientes para el CRUD de los clientes.
- la app 'catálogo' donde se encuentran los modelos y vistas correspondientes para el CRUD de los articulos y las ventas.

2) Se creó un superusuario 'admin' que permite acceder a todas las vistas y opciones, así como acceder a '/admin/'
3) Se limitó el acceso a usuarios que no son 'staff' para poder solo crear o modificar clientes, y ventas, no así eliminar, ni gestionar el catálogo de productos y categorías. 

## Lo pendiente:
- Agregar imágenes, tanto en el menú, como en la descripción de los artículos. 
- Mejorar el diseño de los formularios, para mostrarlo más encuadrado.
- Mejorar el formato en que se visualiza la información referente a fechas.


