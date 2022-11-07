import argparse
import logging
from pyModbusTCP.server import ModbusServer, DataBank

class MyDataBank(DataBank):
    """A custom ModbusServerDataBank for override on_xxx_change methods."""

    def on_coils_change(self, address, from_value, to_value, srv_info):
        """Call by server when change occur on coils space."""
        msg = 'change in coil space [{0!r:^5} > {1!r:^5}] at @ 0x{2:04X} from ip: {3:<15}'
        msg = msg.format(from_value, to_value, address, srv_info.client.address)
        logging.info(msg)

    def on_holding_registers_change(self, address, from_value, to_value, srv_info):
        """Call by server when change occur on holding registers space."""
        msg = 'change in hreg space [{0!r:^5} > {1!r:^5}] at @ 0x{2:04X} from ip: {3:<15}'
        msg = msg.format(from_value, to_value, address, srv_info.client.address)
        logging.info(msg)
