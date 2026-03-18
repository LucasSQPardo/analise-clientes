from utils.constantes import ENVIRONMENT
'''
printa log se ambiente for local, caso contrario, envia para aws (nao implementado)
'''
def sendLog(e) -> None:
    print (e) if(ENVIRONMENT == 'local') else print(e)
