# Autores:
# Lucas Rondon Silveira Ales
# Vítor Laco Bortolotti

from OperatingSystem import *

#O SISTEMA OPERACIONAL ESCOLHIDO FOI O WINDOWS
#O CAMINHO DO EXECUTAVEL PARA SER ABERTO COMO SUBPROGRAMA
#DEVE SER INSERIDO DENTRO DAS ASPAS DA VARIAVEL process_path 
#FEITO ISSO, O ARQUIVO ESTARÁ PRONTO PARA SER EXECUTADO

#caminho do executavel do subprocesso
process_path = r"/usr/bin/drawing"

OS = OperatingSystem()

print('---------INFORMAÇÔES GERAIS DO SISTEMA---------')
#metódo que pega as informações da máquina e escreve na tela
#OS.getInformations()

print('----------INFORMAÇÔES DO SUBPROCESSO-----------')
#metodo que abre o processo e escreve na tela suas informações após seu encerramento
OS.openProcessAndPrintInfo(process_path)

#print("processo")
#print(OS.getProcess(1))