import argparse
import socket

from services.utils import bus_format


class App:
    def __init__(self, login_service, services=[]) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('localhost', 5000)
        print('starting up on %s port %s' % server_address)
        self.socket.bind(server_address)
        self.login_service = login_service
        self.services = services

    def send_msg(self, msg, name='g7999'):
        req = bus_format(msg, name).encode('utf-8')
        self.socket.send(req)
        return self.socket.recv(1024).decode('utf-8')
    
    def login(self):
        inputs = {}
        for i in range(len(self.login_service['inputs'])):
            actual_input = self.login_service['inputs'][i]
            key = actual_input['key']
            inputs[key] = input(actual_input['desc'])
        res = self.send_msg(inputs, self.login_service['id'])
        return res
    
    def show_menu(self):
        while True:
            print("Bienvenido \n")
            print("Menu de opciones:\n")
            print("Opcion 0: Salir \n")
            print("Opcion 1: {}".format(self.login_service['desc']))
            option = input('Ingrese una opcion: ')
            if option == '1':
                res = self.login()
                data = eval(res[12:])
                if res[10:12] == 'NK':
                    print('Servicio no disponible')
                    pass
                elif data == None:
                    print('Login fallido')
                    pass
                else:
                    print('Login exitoso')
                    break
            elif option == '0':
                return
            else:
                print("Opcion no valida")
        self.menu(data[-1])

def menu(self, type_id):
        while True:
            input("Presione enter para continuar")
            print("Bienvenido \n")
            print("Menu de opciones:\n")
            print("Opcion 0: Salir \n")
            available_services = [
                service for service in self.services if type_id in service['user_types']
            ]
            services = {}
            for i in range(len(available_services)):
                actual_service = available_services[i]
                services[f'{i+1}'] = actual_service
                print("Opcion {}: {}".format(i+1, actual_service['desc']))
            print("Opcion 0: Salir")
            option = input('Ingrese una opcion: ')
            if option == '0':
                return
            elif option in services:
                service = services[option]
                inputs = {}
                for i in range(len(service['inputs'])):
                    actual_input = service['inputs'][i]
                    key = actual_input['key']
                    inputs[key] = input(actual_input['desc'])
                res = self.send_message(inputs, service['id'])
                if res[10:12] == 'NK':
                    print('Servicio no disponible')
                    pass
                else:
                    service['function'](res)
            else:
                print("Opcion no valida")

if __name__ == '__main__':
    app = App(
        login_service={
            'id': 'serv1',
            'desc': 'Iniciar sesión',
            'inputs': [
                {
                    'key': 'username',
                    'desc': 'Ingresa tu rut: '
                },
                {
                    'key': 'password',
                    'desc': 'Ingresa tu contraseña: '
                }
            ]
        },
        services=[
            {
                'id': 'serv2',
                'desc': 'Registrar maquinaria',
                'user_types': [0, 1, 2],
                #'function': lambda *_: g_print('maquinaria registrada'),
                'inputs': [
                    {
                        'key': 'nombre',
                        'desc': 'Ingresa el nombre de la maquinaria: ',
                    },
                    {
                        'key': 'estado',
                        'desc': 'Ingresa el estado de la maquinaria: ',
                    },
                    {
                        'key': 'costo',
                        'desc': 'Ingresa el costo de la maquinaria: '
                    }
                ]
            },
            {
                'id': 'serv3',
                'desc': 'Consultar maquinarias',
                'user_types': [0, 1, 2],
                #'function': display_maquinarias,
                'inputs': [
                    {
                        'key': 'id',
                        'desc': 'Ingresa el id de la maquinaria o vacío para consultar por todas: '
                    }
                ]
            },
            {
                'id': 'serv4',
                'desc': 'Modificar maquinaria',
                'user_types': [0, 1, 2],
                #'function': lambda res: g_print('maquinaria modificada') if eval(res[12:]) > 0 else f_print('maquinaria no encontrada'),
                'inputs': [
                    {
                        'key': 'id',
                        'desc': 'Ingresa el id de la maquinaria: '
                    },
                    {
                        'key': 'nombre',
                        'desc': 'Ingresa el nuevo nombre de la maquinaria: ',
                    },
                    {
                        'key': 'estado',
                        'desc': 'Ingresa el nuevo estado de la maquinaria: ',
                    },
                    {
                        'key': 'costo',
                        'desc': 'Ingresa el nuevo costo de la maquinaria: '
                    }
                ]
            }
        ]
    )

    res = app.show_menu()