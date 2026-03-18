from pyspark.sql import SparkSession

from utils.constantes import ARQUIVO_CLIENTES, ARQUIVO_PEDIDOS

def carregarClientes(spark: SparkSession) -> DataFrame:
    print(ARQUIVO_CLIENTES)
    dataFrame = spark.read.format('json').load(ARQUIVO_CLIENTES, header=True, inferSchema=True)
    return dataFrame 


def carregarPedidos(spark: SparkSession) -> DataFrame:
    print(ARQUIVO_PEDIDOS)
    dataFrame = spark.read.format('json').load(ARQUIVO_PEDIDOS, header=True, inferSchema=True)
    return dataFrame 
