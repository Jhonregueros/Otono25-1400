Selecciona: Elige tres opciones de la siguiente lista de cinco (5).
Elabora un documento .py nuevo para cada una de tus tres selecciones.
Guarda los tres documentos en la carpeta 'M12'. Esto constituye la actividad requerida para la semana.
Entregar un enlace de github o subir en carpeta zip.

# TODO #1
Escribe un método __eq__ para la clase Line que devuelva
True si los objetos Line se refieren a objetos Point equivalentes,
en cualquier orden.

# TODO #2
Escribe un método Line llamado midpoint que calcule el punto medio
de un segmento de recta y devuelva el resultado como un objeto Point.

# TODO #3
Escribe un método Rectangle llamado midpoint que encuentre el punto
en el centro de un rectángulo y devuelva el resultado como un objeto Point.

# TODO #4
Escribe un método Rectangle llamado make_cross que haga lo siguiente:
Utiliza make_lines para obtener una lista de objetos Line que representan
los cuatro lados del rectángulo. Calcula los puntos medios de las cuatro líneas.
Crea y devuelve una lista de dos objetos Line que representan líneas que
conectan puntos medios opuestos, formando una cruz por el centro del rectángulo.

# TODO #5
Escribe una definición para una clase llamada Circle con atributos center y radius,
donde center es un objeto Point y radius es un número. Incluye los métodos especiales
__init__ y a __str__, y un método llamado draw que utilice las funciones jupyturtle
para dibujar el círculo.