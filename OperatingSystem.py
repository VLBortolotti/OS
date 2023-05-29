import os
import psutil
import platform
import time
import subprocess

class OperatingSystem():
    def __init__(self):
        pass

    def getInformations(self):
        # Tipo de sistema operacional (Linux / Windows / MacOS, ...)
        tipo_os = platform.system()

        # Versão do sistema operacional
        versao_os = platform.version()

        # Número de processadores
        num_processadores = os.cpu_count()
        
        # Memória RAM total em bytes
        memoria_total = psutil.virtual_memory().total
        
        # Arquitetura do computador
        #arquitetura = os.uname().machine

        # Numero de processos em execução
        num_processos = len(psutil.pids())

        # Memória RAM disponível para uso em Bytes
        memoria_disponivel = psutil.virtual_memory().available

        # Tempo descorrido desde que o PC foi ligado
        uptime = time.time() - psutil.boot_time()
        
        print(f"Tipo de sistema operacional: {tipo_os}")
        print(f"Versão do sistema operacional: {versao_os}")
        #print(f"Arquitetura do computador: {arquitetura}")
        print(f"Memória total: {memoria_total}")
        print(f"Memória disponível {memoria_disponivel}")
        print(f"Número de processadores {num_processadores}")
        print(f"Tempo que o computador está ligado: {uptime} segundos")
        print(f"Número de processos: {num_processos}")

    def getProcess(self, process_id):
        # pegar os dados do processo a partir de seu ID
        process = psutil.Process(process_id)
        
        # numero de trocas de contexto voluntarias
        trocas_context_voluntaria = process.num_ctx_switches().voluntary
        
        # numero de trocas de contexto involuntarias
        trocas_context_involuntaria = process.num_ctx_switches().involuntary

        # numero de sinais recebidos
        sinais_recebidos = process.num_handles()

        # tempo de execucao do processo em segundos
        tempo_execucao = process.create_time()
        
        # memoria utilizada pelo processo em bytes enquanto executava
        memoria_usada = process.memory_info().rss
        
        # Retornar os dados coletados
        data = {}
        data['trocas_context_voluntaria'] = trocas_context_voluntaria
        data['trocas_context_involuntaria'] = trocas_context_involuntaria
        data['sinais_recebidos'] = sinais_recebidos
        data['tempo_execucao'] = tempo_execucao
        data['memoria_usada'] = memoria_usada

        return data

    def openProcessAndPrintInfo(self, process_path):
        try:
            process = subprocess.Popen(process_path)
            process_id = process.pid
        except:
            print('Falha ao iniciar subprocesso e pegar informações')
            exit
        
        return_process_info = False
        while self._processRunning(process_id):
            try:
                process_info = self.getProcess(process_id)
                return_process_info = process_info
            except:
                break

        if return_process_info != False:
            print(f"Trocas de contexto voluntárias: {process_info['trocas_context_voluntaria']}")
            print(f"Trocar de contexto involuntárias: {process_info['trocas_context_involuntaria']}")
            print(f"Sinais recebidos: {process_info['sinais_recebidos']}")
            print(f"Tempo de execução: {process_info['tempo_execucao']}")
            print(f"Memória usada pelo processo: {process_info['memoria_usada']}")
        else:
            print('Falha ao iniciar subprocesso e pegar informações')

    def _processRunning(self, process_id):
        try:
            psutil.Process(process_id)
            return True
        except:
            return False
    