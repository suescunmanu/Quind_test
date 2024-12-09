Análisis de Datos de Alquiler de Películas

Introducción

Este proyecto tiene como propósito crear una aplicación que nos ayude a analizar datos sobre el alquiler de películas. Usamos Python y Spark para trabajar con los datos: los extraemos, los transformamos y los guardamos en un formato más fácil de analizar después.
Objetivos

•	Obtener datos desde una base de datos que incluye información sobre películas, clientes y alquileres.
•	Organizar los datos para que sea más sencillo analizarlos.
•	Guardar los datos transformados en un formato útil para futuros análisis.
•	Usar esos datos para responder preguntas importantes para el negocio.

Tecnologías Utilizadas

•	Python: El lenguaje de programación principal.
•	Spark: Herramienta para manejar grandes volúmenes de datos de forma rápida y eficiente.
•	Pandas: Librería de Python para organizar y analizar datos.
•	SQL: Lenguaje para interactuar con la base de datos y consultar datos.

Estructura del Proyecto

•	etl.py: Aquí está el código principal para extraer, transformar y cargar los datos (ETL).
•	utils.py: Contiene funciones extras que ayudan con tareas comunes.
•	data: Carpeta donde se guardan los datos que se procesan.
•	config.py: Archivo para configurar cosas como la conexión a la base de datos y los nombres de las tablas.

Instalación

1.	Clona el repositorio
git clone https://github.com/suescunmanu/Quind_test.git  
2.	Crea un entorno virtual
python -m venv venv
3.	Activa el entorno virtual
source venv/bin/activate  
4.	En Windows:
venv\Scripts\activate  

Instala las dependencias

pip install -r requirements.txt  

Configuración

Edita el archivo config.py para ajustar lo siguiente:
•	Conexión a la base de datos: Define la URL de conexión, usuario, contraseña y nombre de la base de datos.
•	Tablas a procesar: Especifica las tablas que se van a trabajar.
•	Directorio de salida: La ruta donde se guardarán los archivos generados (CSV).

Ejecucion

python etl.py  

Diseño del Proyecto

•	Arquitectura ETL: Dividimos el proceso en 3 partes: extracción, transformación y carga de datos. Usamos Spark porque es rápido y funciona bien con grandes cantidades de datos.
•	Código modular: Organizamos el código en partes claras para que sea fácil de entender y mantener.
•	Configuración separada: Los ajustes principales están en config.py para no cambiar el código directamente.
•	Funciones auxiliares: Incluimos funciones simples para tareas repetitivas, como conectarse a la base de datos o guardar archivos.

Cómo Contribuir

Si quieres aportar al proyecto:
1.	Realizar un "fork" del repositorio.
2.	Crear una nueva rama para tus cambios.
3.	Realizar los cambios y haz commit.
4.	Envíar un pull request.
   
Licencia

Este proyecto está bajo la licencia MIT.

Próximos Pasos

•	Explorar los datos: Usar herramientas como Pandas o Matplotlib para analizar mejor los datos.
•	Crear visualizaciones: Hacer gráficos para explicar los resultados de manera clara.
•	Desarrollar modelos: Crear predicciones sobre el comportamiento de los clientes o los alquileres.
Otras Consideraciones
•	Agregar comentarios al código para explicar qué hace cada parte.
•	Crear pruebas automáticas para asegurarse de que el código funciona bien.
•	Incluir registros (logs) para rastrear qué está haciendo la aplicación.
•	Usar Docker para que cualquiera pueda instalar y ejecutar el proyecto fácilmente.


