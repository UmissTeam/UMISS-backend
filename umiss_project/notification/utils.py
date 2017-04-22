from pyfcm import FCMNotification


def send_notification(body_signal):
    patient = body_signal.owner
    push_service = FCMNotification(api_key="<api-key>")
    registration_ids = patient.get_monitor_tokens()

    message_title = "Paciente {} Alerta".format(patient)
    message_body = "Hi john, your customized news for today is ready"
    result = push_service.notify_multiple_devices(
        registration_ids=registration_ids,
        message_title=message_title,
        message_body=message_body)
