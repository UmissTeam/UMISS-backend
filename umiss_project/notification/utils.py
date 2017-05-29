from pyfcm import FCMNotification
from fcm_django.models import FCMDevice


def send_notification(body_signal):
    patient = body_signal.owner
    monitor_tokens= patient.get_monitor_tokens()
    message_title = "Paciente {} Alerta".format(patient)
    message_body = "O paciente {0} teve um sinal alterado".format(patient)

    for token in monitor_tokens:
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
