from django.dispatch import receiver
from django_design_pattern_app.signals import signals


# date_time = datetime.datetime.now()
# date_time = formats.date_format(date_time, "SHORT_DATETIME_FORMAT")
# signals.user_visit_signal.send(sender=request ,date_time=date_time,ip=ip,device=request.META['HTTP_USER_AGENT'])


@receiver(signals.user_visit_signal)
def handle_user_visit(sender, date_time, ip, device):
    message = "Visit to view {sender}, at {date_time} , IP is {ip} , Device is {device}".format(sender=sender,
                                                                                                date_time=date_time,
                                                                                                ip=ip, device=device)
    print(message)
