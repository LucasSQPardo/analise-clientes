from utils.logger import sendLog
from utils.carregar_arquivo import carregarClientes, carregarPedidos

from os import sys
from pyspark.sql import SparkSession

def main() -> None:
    try: 
        spark = (
            SparkSession.builder
            .master('local[*]')
            .appName('analise_clientes')
            .getOrCreate()
        )
        clientes = carregarClientes(spark)
        clientes.show(5)
        pedidos = carregarPedidos(spark)
        pedidos.show(5)
    except Exception as e:
        sendLog(e)

if __name__ == '__main__':
    sys.exit(main())
