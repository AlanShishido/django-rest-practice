from django.core.management import BaseCommand
from modbus.master import MasterModbus

class Command(BaseCommand):
    help = 'Start server for Modbus TCP MASTER'

    def add_arguments(self, parser):
        """ Port is an optional parameters """
        parser.add_argument('-p', '--port', type=int, help='Indicates the port to open')

    def handle(self, *args, **options):
        # sender = options['sender_port'] or DEFAULT_SENDER_PORT
        # receiver = options['receiver_port'] or DEFAULT_RECEIVER_PORT
        server = MasterModbus(host_ip='0.0.0.0', port=502)
        print('======================================')
        print('MODBUS TCP MASTER')
        print(f'addres 0.0.0.0:502')
        print('======================================')
        server.run()
