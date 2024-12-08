import pandas as pd
from pyspark.sql import SparkSession
import os

# Crear una SparkSession
spark = SparkSession.builder.appName("rental_analysis").getOrCreate()

# Lista de tablas a procesar
tables = ["film_csv", "inventory_csv", "rental_csv", "customer_csv", "store_csv"]

class ETLTask:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.start_time = None
        self.end_time = None
        self.status = "NOT_STARTED"

    def execute(self):
        self.start_time = datetime.now()
        # Lógica de ejecución de la tarea
        self.end_time = datetime.now()
        self.status = "COMPLETED"

class Extractor(ETLTask):
    def extract_from_db(self, table_names):
        dfs = []
        for table in table_names:
            df = spark.read.table(f"default.{table}")
            dfs.append(df)
        return dfs

class Transformer(ETLTask):
    def transform_data(self, dfs):
        # No se realizan transformaciones, se devuelve la lista de DataFrames
        return dfs

class Loader(ETLTask):
    def load_to_csv(self, dfs, output_dir):
        for i, df in enumerate(dfs):
            output_path = os.path.join(output_dir, f"table_{i}.csv")
            df.toPandas().to_csv(output_path, index=False)

# Crear las tareas ETL
extract_task = Extractor("ExtractData", "Extrae datos de todas las tablas")
transform_task = Transformer("TransformData", "No se realizan transformaciones")
load_task = Loader("LoadData", "Carga los datos a archivos CSV")

# Ejecutar las tareas
all_dfs = extract_task.extract_from_db(tables)
transformed_dfs = transform_task.transform_data(all_dfs)
load_task.load_to_csv(transformed_dfs, "output")