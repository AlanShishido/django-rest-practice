from pyModbusTCP.client import ModbusClient
import random
import logging
from time import sleep

class ClientModbus():
    """
    Classe Cliente Modbus
    """
    def __init__(self, server_ip, port, scan_time=1):
        """
        Construtor
        """
        self._cliente = ModbusClient(host=server_ip, port=port, timeout=20)
        self._scan_time = scan_time
        
    def atendimento(self):
        self._cliente.open()

    def run(self):
        """
        Execução do servidor Modbus
        """
        try:
            self._server.start()
        except Exception as e:
            print(f'Error: {e}')
        self._server.stop()
        
