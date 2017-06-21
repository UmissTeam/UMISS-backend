__author__ = "Tiago ASsuncao"
__copyright__ = "Copyright 2017, The Cogent Project"
__credits__ = ["Tiago Assuncao",]
__license__ = "GPL"
__version__ = "1.1.5"
__maintainer__ = "Tiago Assuncao"
__email__ = "thiagoribeironiquel@hotmail.com"
__status__ = "Production"

"""
This file will create monitors and patients on given server.
You can create many signal, add other values on signals_to_send.
"""

import requests
import random
import string
import argparse


signals_to_send = [
    ('fellchair', 'fellchair'),
    ('heart_beats', 'beats'),
    ('skin_temperatures', 'temperature'),
    ('galvanic_resistances', 'resistance'),
    ('heart_beats', 'beats'),
    ('galvanic_resistances', 'resistance'),
    ('skin_temperatures', 'temperature'),
    ('galvanic_resistances', 'resistance'),
    ('skin_temperatures', 'temperature'),
    ('heart_beats', 'beats'),
    ('skin_temperatures', 'temperature'),
    ('galvanic_resistances', 'resistance'),
    ('skin_temperatures', 'temperature'),
    ('skin_temperatures', 'temperature'),
    ('galvanic_resistances', 'resistance'),
    ('heart_beats', 'beats'),
]


def id_gen(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def prRed(prt): print("\033[91m {}\033[00m" .format(prt))


def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))


def prYellow(prt): print("\033[93m {}\033[00m" .format(prt))


def prLightPurple(prt): print("\033[94m {}\033[00m" .format(prt))


def prPurple(prt): print("\033[95m {}\033[00m" .format(prt))


def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))


def prLightGray(prt): print("\033[97m {}\033[00m" .format(prt))


def prBlack(prt): print("\033[98m {}\033[00m" .format(prt))



token = id_gen(6)
username = id_gen()
# android_token = 'dFn75BRUi9s:APA91bGZAci5gzsV8lbcZAcjepRTSWyI0DGDfPSGzAMjCe60o_q7VkKWY8t21aqhy3FnLqZyQ6AiQv_ZxybK7Pj8YrmJJ4Dpn-Gx5d71cMPusEXozOA-euhyFwAzaHAGgeUD9MmvW2Vv'
android_token = 'asdf'


def print_signals(signals):
    signals = signals['data']
    for signal in signals:
        prPurple("\tSinal: {}".format(signal))

    return len(signals)


def validate_response(response):
    if response.status_code >= 200 and response.status_code < 300:
        prCyan('Ok!')
    else:
        prRed('Error!!!')
        prRed(response.json())


def create_patient():
    patient_response = requests.post(
        url + 'patients',
        data={'username': 'patient_' + username,
              'password': 'asdf1234',
              'token': token
              }
    )

    validate_response(patient_response)
    return patient_response.json()['data']['attributes']


def get_auth_token(user):
    auth_response = requests.post(
        url_auth,
        data={'username': user['username'],
              'password': 'asdf1234',
              }
    )

    validate_response(auth_response)
    user['auth_token'] = auth_response.json()['token']
    return user


def create_monitor():
    monitor_response = requests.post(
        url + 'monitors',
        data={'username': 'monitor_' + username,
              'password': 'asdf1234',
              'token': token,
              'android_token': android_token
              }
    )

    validate_response(monitor_response)
    return monitor_response.json()['data']['attributes']


def create_signals(patient, signal='heart_beats', attribute='beats'):
    value = int(id_gen(3, '011'))
    if signal == 'skin_temperatures':
        value = (value % 6) + 32
    elif signal == 'galvanic_resistances':
        value = (value % 800) + 100

    signal_response = requests.post(
        url + signal,
        data={
            attribute: value,
            'is_critical': True,
        },
        headers={'Authorization': 'Token {}'.format(patient['auth_token'])}
    )

    print(signal_response.json())
    validate_response(signal_response)
    return signal_response


def call_parser():
    parser = argparse.ArgumentParser("simple_example")
    parser.add_argument(
        "server",
        help="IP do servidor com a porta que está rodando.",
        default='localhost:8000',
        type=str)
    args = parser.parse_args()

    global server, url, url_auth
    server = 'http://{}'.format(args.server)
    url = server + '/api/'
    url_auth = server + '/api-auth-token/'

def list_signals(monitor, signal='heart_beats'):
    signal_response = requests.get(
        url + signal,
        headers={'Authorization': 'Token {}'.format(monitor['auth_token'])}
    )

    validate_response(signal_response)
    return signal_response


def call_signals(patient):
    len_signal = len(signals_to_send)
    prGreen('Criando {} sinais...'.format(len_signal))
    for signal_type, attribute in signals_to_send:
        signal = create_signals(patient, signal_type, attribute)
        print(" Signal id: {}".format(signal.json()['data']['id']))

if __name__ == "__main__":
    call_parser()

    prGreen("Aplicando teste no servidor {}".format(server))
    prGreen('Criando paciente...')
    patient = create_patient()
    print(" Paciente {} criado".format(patient['username']))
    prGreen('Autenticando paciente...')
    patient = get_auth_token(patient)

    prGreen('Criando monitor...')
    monitor = create_monitor()
    print(" Monitor {} criado".format(monitor['username']))
    prGreen('Autenticando monitor...')
    monitor = get_auth_token(monitor)

    call_signals(patient)

    prGreen('Listando sinais...')
    list_heart = list_signals(monitor, 'heart_beats').json()
    list_temp = list_signals(monitor, 'skin_temperatures').json()
    list_galvanic = list_signals(monitor, 'galvanic_resistances').json()
    list_fell = list_signals(monitor, 'fellchair').json()

    print(" Signals:")
    total = 0
    total += print_signals(list_heart)
    total += print_signals(list_temp)
    total += print_signals(list_galvanic)
    total += print_signals(list_fell)

    if total == len(signals_to_send):
        prGreen("\n\nSucesso nos testes!")
    else:
        prRed("\n\nAlgo está errado com os testes!!!")
