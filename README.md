# Quind_test
Prueba técnica ingeniero de datos

Análisis de Datos de Alquiler de Películas

Introducción

Este proyecto tiene como objetivo desarrollar una aplicación de análisis de datos que permita explorar y comprender los patrones de alquiler de películas en una base de datos relacional. La aplicación utiliza Python y Spark para extraer, transformar y cargar los datos, proporcionando una base sólida para realizar análisis posteriores.
Objetivos

•	Extraer datos de una base de datos relacional que contenga información sobre películas, alquileres y clientes.
•	Transformar los datos para un análisis más eficiente.
•	Cargar los datos transformados en un formato adecuado para su posterior análisis.
•	Proporcionar una base para realizar análisis exploratorios y responder preguntas de negocio.
Tecnologías Utilizadas
•	Python: Lenguaje de programación principal para la implementación de la aplicación.
•	Spark: Framework de procesamiento de datos a gran escala utilizado para manejar grandes conjuntos de datos de forma eficiente.
•	Pandas: Biblioteca de Python para manipulación y análisis de datos.
•	SQL: Lenguaje de consulta estructurado para interactuar con la base de datos.
Estructura del Proyecto
•	etl.py: Contiene la lógica principal del proceso ETL (Extracción, Transformación, Carga).
•	utils.py: Contiene funciones auxiliares y utilidades comunes.
•	data: Carpeta donde se almacenarán los datos extraídos y transformados.
•	config.py: Archivo de configuración para personalizar los parámetros de la aplicación (por ejemplo, conexión a la base de datos, nombres de tablas).
Instalación
1.	Clonar el repositorio: 
Bash
git clone https://github.com/suescunmanu/Quind_test.git
Usa el código con precaución.
2.	Crear un entorno virtual: 
Bash
python -m venv venv
Usa el código con precaución.
3.	Activar el entorno virtual: 
Bash
source venv/bin/activate  # En Linux/macOS
venv\Scripts\activate  # En Windows
Usa el código con precaución.
4.	Instalar las dependencias: 
Bash
pip install -r requirements.txt
Usa el código con precaución.
Configuración
•	Archivo config.py: Modifica el archivo config.py para especificar los siguientes parámetros: 
o	Conexión a la base de datos: URL de conexión, usuario, contraseña, base de datos.
o	Tablas a procesar: Lista de nombres de tablas a extraer.
o	Directorio de salida: Ruta donde se guardarán los archivos CSV.
Ejecución
Para ejecutar la aplicación:
Bash
python etl.py
Usa el código con precaución.
Diseño y Justificación
•	Arquitectura ETL: Se ha adoptado una arquitectura ETL clásica para separar claramente las etapas del proceso. Spark se utiliza para la extracción y transformación debido a su escalabilidad y eficiencia en el manejo de grandes conjuntos de datos.
•	Modularidad: El código se divide en módulos bien definidos para mejorar la legibilidad y mantenibilidad.
•	Configuración externa: Los parámetros de configuración se almacenan en un archivo separado para facilitar los cambios y evitar modificar el código directamente.
•	Funciones auxiliares: Se han creado funciones auxiliares para realizar tareas comunes, como la conexión a la base de datos y la escritura de archivos CSV.
Contribuciones
Las contribuciones son bienvenidas. Para contribuir, sigue estos pasos:
1.	Forkea el repositorio.
2.	Crea una nueva rama para tu característica.
3.	Realiza los cambios y haz commit.
4.	Envía un pull request.
Licencia
Este proyecto está bajo la licencia MIT.
Próximos Pasos
•	Análisis exploratorio: Realizar un análisis más profundo de los datos utilizando herramientas como pandas y matplotlib.
•	Visualización: Crear visualizaciones para comunicar los resultados de manera efectiva.
•	Modelado: Desarrollar modelos predictivos para predecir el comportamiento de los usuarios.
Consideraciones Adicionales:
•	Documentación de funciones: Agrega comentarios detallados dentro del código para explicar la lógica de cada función.
•	Pruebas unitarias: Implementa pruebas unitarias para garantizar la calidad del código.
•	Logs: Agrega registros para facilitar la depuración y el seguimiento del proceso.
•	Docker: Considera utilizar Docker para crear un entorno de desarrollo reproducible.
Este README proporciona una base sólida para tu proyecto. A medida que el proyecto evolucione, puedes agregar más secciones y detalles según sea necesario.


