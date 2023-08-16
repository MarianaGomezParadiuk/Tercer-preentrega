WEB Django para una biblioteca.
Autor: Gómez Paradiuk Mariana
Fecha: 08/2023

-------------------------------------------------
Modelos utilizados:

- Lector
    nombre = CharField
    apellido = CharField
    direccion = CharField
    email = EmailField
    telefono = IntegerField
    
- Bibliotecario
    nombre = CharField
    apellido = CharField
    contacto = CharField
    
- Libro
    titulo = CharField
    tipo = CharField
    autor = CharField
    editorial = CharField
    cantidad = IntegerField
    
- Pedido
    titulo = CharField
    id_lector = IntegerField

-------------------------------------------------
Urls disponibles:

    - home
    - db
    - pedidoForm
    - registroForm
    - aplicanteForm
    - libroForm
    - buscarLibro (Busqueda por título)
    - buscar

--------------------------------------------------
El objetivo de la web es permitir carga de datos de todos los modelos por medio de formularios y la busqueda (filtro) dentro de alguna categoría de un modelo. También se crea una pantalla para mostrar todos los datos almacenados dentro de la BD asociada a la web.

Para darle cierto realismo se laenmarca en el contexto de una biblioteca universitaria donde los alumnos y/o profesores serían los lectores, el modelo bibliotecario se utiliza para posibles postulantes, los pedidos serán reservas de material asociados a un lector, y los libros serán los materiales disponibles en nuestra biblioteca.