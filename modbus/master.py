from pyModbusTCP.server import ModbusServer, DataBank
from modbus.handler import MyDataHandler
from modbus.databank import MyDataBank
import random
import os
import logging
from time import sleep

class MasterModbus():
    """
    Classe Servidor Modbus
    """
    def __init__(self, host_ip, port):
        """
        Construtor
        """
        self._db = DataBank()
        self._server = ModbusServer(host=host_ip, port=port, no_block=True, data_bank=self._db)
        

    def run(self):
        """
        Execução do servidor Modbus
        """
        try:
            self._server.start()
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                _h00_bit_list = self._server.data_bank.get_coils(address=0x00, number=10)
                _h01_bit_list = self._server.data_bank.get_discrete_inputs(address=0x00, number=10)
                _h03_word_list = self._server.data_bank.get_input_registers(address=0x00, number=10)
                _h04_word_list = self._server.data_bank.get_holding_registers(address=0x00, number=10)
                if self._server.is_run:
                    boolean_list = self._server.data_bank.get_coils(address=0)
                    if boolean_list[0] == False:
                        self._server.data_bank.set_holding_registers(address=0, word_list=[1])
                    self._server.data_bank.set_coils(address=0, bit_list=[True])
                    self._server.data_bank.set_discrete_inputs(address=0, bit_list=[True])
                    self._server.data_bank.set_holding_registers(address=0, word_list=[10])
                    self._db.set_holding_registers(address=3, word_list=[10])
                    teste = [1,random.randrange(int(0.95*400), int(1.05*400))]
                    self._server.data_bank.set_input_registers(address=15, word_list=teste)
                    print(f'TABELA\r\n {self._server.data_bank.get_holding_registers(address=0, number=3)}')
                    print(_h00_bit_list)
                    print(_h01_bit_list)
                    print(_h03_word_list)
                    print(_h04_word_list)
                    
                sleep(1)
        except Exception as e:
            print(f'Error: {e}')
        self._server.stop()
        
