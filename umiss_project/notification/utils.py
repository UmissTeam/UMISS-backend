from pyfcm import FCMNotification
from fcm_django.models import FCMDevice


def send_notification(body_signal, msg="O paciente {0} teve um sinal alterado"):
    patient = body_signal.owner
    monitor_tokens = patient.get_monitor_tokens()
    message_title = "Paciente {} Alerta".format(patient)
    # message_body = msg.format(patient)
    message_body = "O paciente {} teve um sinal de {} alterado".format(patient, str(body_signal))
    print(message_body, monitor_tokens, patient)

    for token in monitor_tokens:
        if token is not None:
            device = FCMDevice(registration_id=token, type='android')
            data_message = {
                    "Type": "ALERTA",
                    "Title": message_title,
                    "Body": message_body
                    }
            device.send_message(
                    title=message_title,
                    body=message_body,
                    data=data_message)

def logout_notify(token):        
    device = FCMDevice(registration_id=token, type='android')
    data_message = {"Type": "LOGOUT"}
    device.send_message(data=data_message)

